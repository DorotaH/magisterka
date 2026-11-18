"""Execute one benchmark probe inside the external process sandbox."""

from collections import Counter, OrderedDict, defaultdict, deque
from collections.abc import Iterator
from bisect import bisect_left, bisect_right
from functools import cache, lru_cache
from heapq import heappop, heappush, heapify
from itertools import permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
import importlib
import copy
from dataclasses import dataclass
import importlib.util
import io
import json
from pathlib import Path
import random
import re
import sys
import typing
import unittest
from xml.etree import ElementTree

from contextlib import redirect_stdout


@dataclass(eq=False)
class ListNode:
    val: int = 0
    next: "ListNode | None" = None


@dataclass(eq=False)
class TreeNode:
    val: int = 0
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def encode_nodes(root, links):
    pending = [root]
    indexes = {id(root): 0}
    records = []
    for node in pending:
        if len(pending) > 10_000:
            raise ValueError("result graph exceeds serialization limit")
        edges = {}
        for attr in links:
            child = getattr(node, attr)
            if child is None:
                edges[attr] = None
                continue
            if id(child) not in indexes:
                indexes[id(child)] = len(pending)
                pending.append(child)
            edges[attr] = indexes[id(child)]
        records.append({"value": node.val, **edges})
    return {"node_graph": records}


def normalize(value):
    type_name = type(value).__name__
    if type_name == "ListNode" and all(hasattr(value, key) for key in ("val", "next")):
        return encode_nodes(value, ("next",))
    if type_name == "TreeNode" and all(hasattr(value, key) for key in ("val", "left", "right")):
        return encode_nodes(value, ("left", "right"))
    if isinstance(value, ElementTree.Element):
        return {"xml": ElementTree.tostring(value, encoding="unicode")}
    if isinstance(value, (set, frozenset)):
        return sorted(value, key=repr)
    if isinstance(value, Iterator):
        return {"iterator_type": type_name}
    return re.sub(r" at 0x[0-9a-fA-F]+(?=>)", "", repr(value))


def scope(mercury=False):
    initial = {name: getattr(typing, name) for name in typing.__all__}
    initial.update(TreeNode=TreeNode, ListNode=ListNode, Counter=Counter, defaultdict=defaultdict,
                   deque=deque, __name__="benchmark_solution")
    if mercury:
        modules = ("re", "itertools", "collections", "heapq", "bisect", "string",
                   "sys", "lctk", "functools", "math", "copy", "sortedcontainers")
        initial.update({name: importlib.import_module(name) for name in modules})
        initial.update({name: globals()[name] for name in
                        ("floor", "ceil", "factorial", "sqrt", "inf", "bisect_left", "bisect_right",
                         "permutations", "zip_longest", "heappush", "heappop", "heapify",
                         "OrderedDict", "lru_cache", "cache")})
        initial.update(maxsize=sys.maxsize, stdin=sys.stdin)
    return initial


def source_namespace(path, mercury=False):
    env = scope(mercury)
    exec(compile(Path(path).read_text(), path, "exec"), env)
    return env


def stable_json(value):
    return json.dumps(value, default=normalize, sort_keys=True)


def mercury_generate(payload):
    env = scope(mercury=True)
    exec(payload["generator_code"], env)
    raw = [env["generate_test_case"]() for _ in range(payload["limit"])]
    arity = len(payload["official"][0]["input"])
    # Generic scalar generators usually return a single argument, while
    # multi-argument generators return the positional arguments together.
    return [[value] if arity == 1 else list(value) for value in raw]


def mercury_execute(payload, path):
    env = source_namespace(path, mercury=True)
    exec(payload["convert_offline"], env)
    exec(payload["evaluate_offline"], env)
    errors = []
    outputs = []
    verdicts = []
    for case in payload["cases"]:
        try:
            args, expected = env["convert_offline"](copy.deepcopy((case["input"], case.get("expected"))))
            function = getattr(env["Solution"](), payload["entry_point"])
            result = function(*args)
            if isinstance(result, (map, filter, zip, reversed)):
                result = list(result)
            verdict = env["evaluate_offline"](args, result, expected) if "expected" in case else None
            verdicts.append(verdict)
            outputs.append(stable_json(result))
            errors.append(None)
        except Exception as error:
            errors.append(f"{type(error).__name__}: {error}")
            outputs.append(None)
            verdicts.append(None)
    return {"outputs": outputs, "verdicts": verdicts, "errors": errors}


def apps_call(payload, path):
    env = source_namespace(path)
    function_name = payload["fn_name"]
    if "Solution" not in env:
        function = env[function_name]
    else:
        function = getattr(env["Solution"](), function_name)
    result = function(*payload["input"])
    return {"result": stable_json(result)}


def classeval(payload, path):
    from contextlib import nullcontext

    name = "benchmark_case"
    spec = importlib.util.spec_from_loader(name, loader=None)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    checks = {}
    test_ids = []
    stack = []
    original_run = unittest.TestCase.run
    observed = {}
    call_depth = 0

    def observe(frame, event, value):
        nonlocal call_depth
        if not stack or frame.f_code.co_filename != path:
            return
        if frame.f_code.co_name.startswith("<"):
            return
        if event == "call":
            call_depth += 1
        elif event == "return":
            call_depth -= 1
            if call_depth == 0:
                name = frame.f_code.co_name
                try:
                    result = stable_json(value)
                except (ValueError, TypeError):
                    result = type(value).__name__
                observed.setdefault(stack[-1], []).append([name, result])


    def trace_run(self, result=None):
        test_ids.append(self.id())
        stack.append(self.id())
        try:
            return original_run(self, result)
        finally:
            stack.pop()

    def trace(assert_name, assertion):
        def wrapper(self, *args, **kwargs):
            if stack:
                checks.setdefault(stack[-1], []).append([assert_name, len(args)])
            return assertion(self, *args, **kwargs)
        return wrapper

    unittest.TestCase.run = trace_run
    for name in dir(unittest.TestCase):
        if name.startswith("assert") and callable(assertion := getattr(unittest.TestCase, name)):
            setattr(unittest.TestCase, name, trace(name, assertion))
    freezer = nullcontext()
    if payload.get("freeze"):
        from freezegun import freeze_time
        freezer = freeze_time(payload["freeze"])
    with freezer:
        exec(compile(Path(path).read_text(), path, "exec"), vars(module))
        exec(compile(payload["test"], "<official-test>", "exec"), vars(module))
        suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(getattr(module, name.strip()))
                                  for name in payload["test_classes"])
        log = io.StringIO()
        sys.setprofile(observe)
        try:
            result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
        finally:
            sys.setprofile(None)
    return {"tests": result.testsRun, "pass": result.wasSuccessful(), "test_ids": test_ids,
            "checks": checks, "observed": observed, "failures": [test.id() for test, _ in result.failures],
            "errors": [test.id() for test, _ in result.errors], "log": log.getvalue()}


def main():
    mode, data, *path = sys.argv[1:]
    payload = json.loads(Path(data).read_text())
    random.seed(payload.get("seed", 20261118))
    logs = io.StringIO()
    with redirect_stdout(logs):
        if mode == "mercury_generate":
            answer = mercury_generate(payload)
        elif mode == "mercury":
            answer = mercury_execute(payload, path[0])
        elif mode == "apps_call":
            answer = apps_call(payload, path[0])
        else:
            answer = classeval(payload, path[0])
    print(stable_json({"answer": answer, "stdout": logs.getvalue()}))


if __name__ == "__main__":
    main()
