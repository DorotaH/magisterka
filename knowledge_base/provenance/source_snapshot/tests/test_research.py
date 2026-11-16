import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from measure_research import load_checkpoint
from research_metrics import measure_artifact, measure_radon
from report_knowledge import bootstrap_mean, wilson


class ResearchRegressionTests(unittest.TestCase):
    def test_one_tool_failure_keeps_other_results(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "code.py"
            data = b"def f(x):\r\n    return x + 1\r\n"
            path.write_bytes(data)
            with patch(
                "research_metrics.measure_complexipy",
                side_effect=ValueError("test failure"),
            ):
                row = measure_artifact(
                    ("sample", str(path), hashlib.sha256(data).hexdigest())
                )
            states = {r["tool"]: r["status"] for r in row["measurements"]}
            self.assertEqual(
                states, {"ruff": "ok", "complexipy": "tool_error", "radon": "ok"}
            )
            self.assertEqual(path.read_bytes(), data)

    def test_radon_does_not_double_count_methods_or_skip_closures(self):
        code = "class C:\n    def f(self,x):\n        def g(y):\n            if y:\n                return 1\n            return 0\n        if x:\n            return g(x)\n        return 0\n"
        result = measure_radon(code)
        self.assertEqual(result["metrics"]["cc.function_count"], 2)
        self.assertEqual(result["metrics"]["cc.function_total"], 4)

    def test_changed_input_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "code.py"
            path.write_text("x=1\n")
            with self.assertRaisesRegex(RuntimeError, "hash mismatch"):
                measure_artifact(("sample", str(path), "0" * 64))

    def test_checkpoint_recovers_only_a_truncated_last_record(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "rows.jsonl"
            good = json.dumps({"artifact_id": "one"}) + "\n"
            path.write_bytes(good.encode() + b'{"artifact_id":')
            self.assertEqual(set(load_checkpoint(path)), {"one"})
            self.assertEqual(path.read_bytes(), good.encode())
            self.assertEqual(
                path.with_name("rows.jsonl.incomplete-tail").read_bytes(),
                b'{"artifact_id":',
            )

    def test_complete_checkpoint_record_without_newline_is_appendable(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "rows.jsonl"
            path.write_text(json.dumps({"artifact_id": "one"}))
            load_checkpoint(path)
            with path.open("a") as stream:
                stream.write(json.dumps({"artifact_id": "two"}) + "\n")
            self.assertEqual(set(load_checkpoint(path)), {"one", "two"})

    def test_intervals_are_defined_for_constant_and_empty_data(self):
        self.assertEqual(bootstrap_mean([0, 0, 0], "test", 100), (0, 0))
        self.assertEqual(wilson(0, 0), (None, None))
        low, high = wilson(0, 100)
        self.assertAlmostEqual(low, 0)
        self.assertGreater(high, 0)
        self.assertLess(high, 1)


if __name__ == "__main__":
    unittest.main()
