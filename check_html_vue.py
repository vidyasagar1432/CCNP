#!/usr/bin/env python3
"""check_html_vue.py — headless regression check for Vue-powered HTML pages.

Runs on any page with a <div id="app"> root (defaults to the EIGRP deep-dive,
works for any page using the vault's local vue.global.prod.js):

  1. Structural checks (Python, no node needed)
       - {{ mustache }} balance inside the #app block
       - tag balance (<section> <div> <pre> <button> <table> ...)
       - zero same-element v-if + v-for pairs
  2. Compile check (node + the exact vue.global.prod.js the vault ships)
       - the #app template must compile
       - every inline <script> must be syntactically valid
  3. Headless render (node)
       - executes the compiled render function against the page's real
         setup() state (refs unwrapped like Vue's instance proxy)
       - catches mount-time crashes like
         "TypeError: can't access property 'key', c is undefined"
  4. App-state smoke tests (EIGRP page)
       - DUAL feasibility verdicts (RD<FD / RD=FD / RD>FD)
       - EIGRP metric math (classic + wide)
       - convergence simulator transitions
       - quiz answer-all-correct scoring
       - checklist toggling and command-viewer switching

Pages with a different mount style (e.g. `index.html` with app.mount(...))
still get checks 1-3; check 4 is skipped with a note.

Usage:
    python3 check_html_vue.py [page.html]
    python3 check_html_vue.py                     # Level 11 - EIGRP/How EIGRP Works.html

Exit code 0 = all checks passed, 1 = something failed.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_HTML = SCRIPT_DIR / "Level 11 - EIGRP" / "How EIGRP Works.html"

# ---------------------------------------------------------------------------
# The node payload: minimal DOM stub + compile/render/state harness.
# argv[2] = html path, argv[3] = vue bundle path. ASCII-safe output.
# ---------------------------------------------------------------------------
DOM_STUB_JS = r"""
function decodeEntities(s) {
  return String(s)
    .replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"').replace(/&apos;/g, "'").replace(/&nbsp;/g, " ")
    .replace(/&#(\d+);/g, (m, n) => String.fromCharCode(Number(n)))
    .replace(/&#x([0-9a-fA-F]+);/g, (m, n) => String.fromCharCode(parseInt(n, 16)));
}
function makeEl(tag) {
  const el = {
    tagName: String(tag || "div").toUpperCase(),
    nodeType: 1, children: [], style: {}, attrs: {},
    className: "",
    classList: { add() {}, remove() {}, toggle() {}, contains() { return false; } },
    dataset: {},
    setAttribute(k, v) { this.attrs[k] = String(v); },
    getAttribute(k) { return k in this.attrs ? this.attrs[k] : null; },
    removeAttribute(k) { delete this.attrs[k]; },
    hasAttribute(k) { return k in this.attrs; },
    appendChild(c) { this.children.push(c); c.parentNode = this; return c; },
    insertBefore(c, r) { this.children.push(c); c.parentNode = this; return c; },
    removeChild(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); return c; },
    replaceChild(n, o) { const i = this.children.indexOf(o); if (i >= 0) this.children[i] = n; n.parentNode = this; return o; },
    addEventListener() {}, removeEventListener() {},
    querySelector() { return null; }, querySelectorAll() { return []; },
    contains() { return false; }, closest() { return null; },
    cloneNode() { return makeEl(this.tagName); },
    focus() {}, blur() {}, click() {}, matches() { return false; },
    getBoundingClientRect() { return { top: 0, left: 0, width: 0, height: 0 }; },
    parentNode: null, nextSibling: null, firstChild: null,
    textContent: "", value: "", checked: false, disabled: false
  };
  Object.defineProperty(el, "innerHTML", {
    get() { return this._innerHTML || ""; },
    set(v) {
      this._innerHTML = String(v);
      const m = String(v).match(/^<div\s+(\w+)\s*=\s*"([^"]*)"\s*>$/);
      if (m) {
        const child = makeEl("div");
        child.attrs[m[1]] = decodeEntities(m[2]);
        this.children = [child]; child.parentNode = this;
      } else {
        this.children = [];
      }
      this.textContent = this._innerHTML ? decodeEntities(this._innerHTML) : "";
      this.firstChild = this.children[0] || null;
    }
  });
  return el;
}
const documentStub = {
  nodeType: 9,
  createElement: t => makeEl(t),
  createElementNS: (ns, t) => makeEl(t),
  createTextNode: t => ({ nodeType: 3, textContent: String(t), data: String(t) }),
  createComment: t => ({ nodeType: 8, textContent: String(t) }),
  createDocumentFragment: () => makeEl("#fragment"),
  querySelector: () => null,
  querySelectorAll: () => [],
  getElementById: () => null,
  documentElement: makeEl("html"),
  head: makeEl("head"),
  body: makeEl("body"),
  addEventListener() {}, removeEventListener() {},
  defaultView: null
};
"""

HARNESS_JS = r"""
"use strict";
const fs = require("fs"), vm = require("vm");
const htmlPath = process.argv[2], vuePath = process.argv[3];
const html = fs.readFileSync(htmlPath, "utf8");
const vueSrc = fs.readFileSync(vuePath, "utf8");

let failures = 0;
const ok   = (...a) => console.log("  [ok]   ", ...a);
const skip = (...a) => console.log("  [skip] ", ...a);
const fail = (...a) => { failures++; console.log("  [FAIL] ", ...a); };

function finish() {
  console.log(failures ? "  -> FAILED (" + failures + " problem" + (failures === 1 ? "" : "s") + ")"
                       : "  -> all node checks passed");
  process.exit(failures ? 1 : 0);
}

/* ---------- sandbox ---------- */
const store = {};
const sandbox = {
  console, setTimeout, clearTimeout, document: documentStub,
  localStorage: {
    getItem: k => (k in store ? store[k] : null),
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: k => { delete store[k]; }
  }
};
let Vue;
try {
  vm.createContext(sandbox);
  vm.runInContext(vueSrc, sandbox);
  Vue = sandbox.Vue;
} catch (e) { fail("loading vue bundle:", e.message); finish(); }

/* ---------- locate the #app template ---------- */
const start = html.indexOf('<div id="app"');
let end = html.indexOf('</div>\n\n<script', start);
if (end >= 0) end += '</div>'.length;          // include the closing </div>
if (end < 0) {
  const bodyIdx = html.indexOf("</body>");
  end = html.lastIndexOf("</div>", bodyIdx) + '</div>'.length;
}
if (start < 0 || end < 0 || end <= start) { fail("cannot locate <div id=\"app\"> template"); finish(); }
const template = html.slice(start, end);

/* ---------- inline <script> syntax (no src= tags) ---------- */
const scripts = Array.from(html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g));
if (scripts.length) {
  let allOk = true;
  for (const m of scripts) {
    try { new Function(m[1]); }
    catch (e) { allOk = false; fail("inline <script> syntax:", e.message); }
  }
  if (allOk) ok("inline <script> syntax (" + scripts.length + " block" + (scripts.length === 1 ? "" : "s") + ")");
} else {
  skip("no inline <script> blocks");
}

/* ---------- compile ---------- */
let render = null;
try {
  render = Vue.compile(template);
  if (typeof render !== "function") throw new Error("unexpected compile result: " + typeof render);
  ok("template compiles (" + template.length + " chars)");
} catch (e) { fail("template compile:", e.message); finish(); }

/* ---------- extract and evaluate setup() (EIGRP-page style) ---------- */
const sm = html.match(/createApp\(\{([\s\S]*?)\n\s*\}\)\.mount\(/);
if (!sm) {
  skip("setup body not found (different mount style) - render/state checks are EIGRP-page only");
  finish();
}
const body = sm[1];
const setupSrc = "(function(){"
  + " const { ref, computed } = globalThis.__vue;"
  + " const LS={theme:'ccnp.eigrp.theme',done:'ccnp.eigrp.done',quizbest:'ccnp.eigrp.quizbest'};"
  + " function loadJSON(key,fb){try{const v=JSON.parse(localStorage.getItem(key));return v??fb}catch{return fb}}"
  + " function save(key,val){localStorage.setItem(key,JSON.stringify(val))}"
  + " function shuffle(a){const x=a.slice();for(let i=x.length-1;i>0;i--){"
  +   "const j=Math.floor(Math.random()*(i+1));[x[i],x[j]]=[x[j],x[i]]}return x}"
  + " return ({" + body + "\n}); })()";
sandbox.__vue = Vue;
let state = null;
try {
  const options = vm.runInContext(setupSrc, sandbox);
  state = options.setup();
} catch (e) {
  skip("evaluating setup() (not the EIGRP page?): " + e.message);
  finish();
}

/* ---------- instance-proxy emulation (refs unwrap like in the browser) ---------- */
function unwrap(v) { return (v && v.__v_isRef && !v.__v_isShallow && "value" in v) ? v.value : v; }
const ctx = new Proxy(state, {
  has: (t, k) => typeof k === "string" ? k in t : false,
  get: (t, k) => {
    if (k === Symbol.unscopables) return undefined;
    return k in t ? unwrap(t[k]) : undefined;
  },
  set: (t, k, v) => {
    if (k in t && t[k] && t[k].__v_isRef) { t[k].value = v; return true; }
    t[k] = v; return true;
  }
});

/* ---------- execute the render function (mount-time crash surface) ---------- */
try {
  const vnode = render(ctx, []);
  const kids = Array.isArray(vnode.children) ? vnode.children.length : "n/a";
  ok("render OK (vnode type: " + vnode.type + ", children: " + kids + ")");
} catch (e) { fail("render:", e.message); finish(); }

/* ---------- app-state smoke tests (skip gracefully if bindings differ) ---------- */
const need = (stateObj, ...keys) => {
  for (const k of keys) if (!(k in stateObj)) throw new Error("missing state." + k + " - skipped");
};
const T = (name, fn) => {
  try { fn(); ok("state:  " + name); }
  catch (e) {
    if (/^missing state\./.test(e.message)) skip(e.message);
    else fail("state:  " + name, "-", e.message);
  }
};

T("fcVerdict RD<FD", () => {
  need(state, "fcVerdict");
  if (state.fcVerdict.value.cls !== "fs") throw new Error("expected 'fs' verdict");
});
T("fcVerdict RD=FD", () => {
  state.rd.value = 20;
  if (state.fcVerdict.value.cls !== "eq") throw new Error("expected 'eq' verdict");
});
T("fcVerdict RD>FD", () => {
  state.rd.value = 30;
  if (state.fcVerdict.value.cls !== "no") throw new Error("expected 'no' verdict");
});
T("metric math (classic + wide)", () => {
  need(state, "bw", "dly", "classicMetric", "wideMetric");
  state.bw.value = 1000; state.dly.value = 100;
  if (state.classicMetric.value !== 2562560) throw new Error("classic = " + state.classicMetric.value);
  if (state.wideMetric.value !== 656015360) throw new Error("wide = " + state.wideMetric.value);
});
T("scenario switch -> 3 paths", () => {
  need(state, "setScenario", "paths");
  state.setScenario(2);
  if (state.paths.value.length !== 3) throw new Error("expected 3 paths, got " + state.paths.value.length);
});
T("failLink starts DUAL sim", () => {
  need(state, "failLink", "failed");
  state.failLink();
  if (!state.failed.value) throw new Error("failed flag not set");
});
T("adjacency animation start/reset", () => {
  need(state, "playAdj", "resetAdj", "adjRunning");
  state.playAdj();
  if (!state.adjRunning.value) throw new Error("adjRunning not set after playAdj");
  state.resetAdj();
  if (state.adjRunning.value) throw new Error("adjRunning not cleared by resetAdj");
});
T("quiz: answer all correctly -> full score", () => {
  need(state, "quizQuestions", "submitQuiz", "quizDone", "quizScore");
  for (const q of state.quizQuestions.value) {
    q.picked = q.options.findIndex(o => o.text === q.answerText);
    if (q.picked < 0) throw new Error("correct answer not found among options");
  }
  state.submitQuiz();
  if (!state.quizDone.value) throw new Error("quiz not marked done");
  if (state.quizScore.value !== state.quizQuestions.value.length) throw new Error("score = " + state.quizScore.value);
});
T("checklist toggle", () => {
  need(state, "toggleDone", "done", "doneCount");
  state.toggleDone(0);
  if (!state.done.value[0]) throw new Error("done[0] not set");
  if (state.doneCount.value < 1) throw new Error("doneCount not updated");
});
T("command viewer switch", () => {
  need(state, "activeCmd", "activeCommand");
  if (!state.activeCommand.value || state.activeCommand.value.key !== "neighbors") throw new Error("initial command wrong");
  state.activeCmd.value = "topology";
  if (state.activeCommand.value.key !== "topology") throw new Error("switch to topology failed");
});

finish();
"""


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def find_node():
    node = shutil.which("node")
    if node:
        return node
    print("ERROR: node.js not found on PATH - needed to compile the Vue template", file=sys.stderr)
    print("       install it or add it to PATH, then re-run.", file=sys.stderr)
    sys.exit(1)


def find_vue_bundle(html_path: Path) -> Path:
    """Locate vue.global.prod.js: next to the html, one level up, or next to this script."""
    candidates = [
        html_path.parent / "vue.global.prod.js",
        html_path.parent.parent / "vue.global.prod.js",
        SCRIPT_DIR / "vue.global.prod.js",
    ]
    for c in candidates:
        if c.is_file():
            return c
    print("ERROR: could not find vue.global.prod.js (looked in: {})".format(
        ", ".join(str(c) for c in candidates)), file=sys.stderr)
    sys.exit(1)


def app_block(html: str) -> str:
    start = html.find('<div id="app"')
    if start < 0:
        return ""
    end = html.find('</div>\n\n<script', start)
    if end >= 0:
        end += len('</div>')                     # include the closing </div>
    else:
        body = html.find("</body>")
        end = html.rfind("</div>", start, body if body > start else len(html))
        if end >= 0:
            end += len('</div>')
    if end <= start:
        return ""
    return html[start:end]


def structural_checks(html: str) -> list:
    """Python-native checks that don't need node."""
    problems = []
    block = app_block(html)
    if not block:
        return ['cannot locate <div id="app"> template']
    opens = block.count("{{")
    closes = block.count("}}")
    if opens != closes:
        problems.append("mustache imbalance: {} '{{' vs {} '}}'".format(opens, closes))
    for tag in ("section", "div", "pre", "button", "table", "nav", "header", "footer"):
        o = len(re.findall(r"<{}(\s|>)".format(tag), block))
        c = len(re.findall(r"</{}>".format(tag), block))
        if o != c:
            problems.append("<{}>: {} open vs {} close".format(tag, o, c))
    same_node = re.findall(r'v-for="[^"]*"[^>]*v-if=|v-if="[^"]*"[^>]*v-for=', block)
    if same_node:
        problems.append("{} same-element v-if+v-for pair(s) - v-if wins, loop var is undefined".format(len(same_node)))
    return problems


def run_node_harness(node: str, html_path: Path, vue_path: Path) -> int:
    payload = DOM_STUB_JS + HARNESS_JS
    fd, tmp = tempfile.mkstemp(suffix=".js", prefix="check-html-vue-", text=True)
    try:
        with os.fdopen(fd, "w") as fh:
            fh.write(payload)
        proc = subprocess.run(
            [node, tmp, str(html_path), str(vue_path)],
            capture_output=True, text=True,
        )
        for line in (proc.stdout or "").splitlines():
            print(line)
        if proc.stderr and proc.stderr.strip():
            print("  [stderr]", proc.stderr.strip(), file=sys.stderr)
        return proc.returncode
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Headless regression check for Vue-powered HTML pages in this vault.")
    parser.add_argument("page", nargs="?", default=str(DEFAULT_HTML),
                        help="HTML file to check (default: Level 11 - EIGRP/How EIGRP Works.html)")
    parser.add_argument("--list-checks", action="store_true",
                        help="print what the script checks and exit")
    args = parser.parse_args()

    if args.list_checks:
        print("Checks performed by this script:")
        print("  1. structure  - mustache/tag balance in #app, no same-element v-if+v-for (python)")
        print("  2. compile    - #app template compiles with the vault's vue.global.prod.js (node)")
        print("  3. syntax     - every inline <script> in the page parses (node)")
        print("  4. render     - compiled render runs against real setup() state (node)")
        print("  5. state      - EIGRP-page smoke tests: DUAL verdicts, metric math, simulators,")
        print("                   quiz all-correct scoring, checklist, command viewer (node)")
        return 0

    html_path = Path(args.page).resolve()
    if not html_path.is_file():
        print("ERROR: page not found: {}".format(html_path), file=sys.stderr)
        return 1

    node = find_node()
    vue_path = find_vue_bundle(html_path)

    print("Checking: {}".format(html_path))
    print("Vue bundle: {}".format(vue_path))
    print("Node: {}".format(node))
    print()

    problems = structural_checks(html_path.read_text(encoding="utf-8"))
    if problems:
        for p in problems:
            print("  [FAIL] structure:", p)
        print()
        print("RESULT: FAILED (structural problems) - fix before re-running")
        return 1
    print("  [ok]   structure: mustaches balanced, tags balanced, no same-element v-if+v-for")
    print()

    code = run_node_harness(node, html_path, vue_path)
    print()
    if code == 0:
        print("RESULT: ALL CHECKS PASSED")
    else:
        print("RESULT: FAILED (see [FAIL] lines above)")
    return code


if __name__ == "__main__":
    sys.exit(main())