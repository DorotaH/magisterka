import unittest

from detect_ruff import ruff_exact, transitions
from run_mbpp import normalize_sew_verdicts


class DetectionRegressionTests(unittest.TestCase):
    def test_low_p_without_minimum_evidence_is_not_a_detection(self):
        row = dict(method='sew', status='ok', original_detected=False,
                   watermarked_detected=True,
                   original_detection={'p': 1, 'verdict': 'No watermark evidence'},
                   watermarked_detection={'p': 0.004256, 'n_grades': 4,
                                          'verdict': 'Insufficient evidence'})
        result = normalize_sew_verdicts(row)
        self.assertFalse(result['watermarked_detected'])
        self.assertTrue(result['legacy_p_only']['watermarked_detected'])

    def test_formatter_preserves_crlf_without_text_mode_translation(self):
        code = 'def f():\r\n    return 1\r\n'
        output = ruff_exact('format', code)
        self.assertEqual(output.encode('utf-8'), code.encode('utf-8'))

    def test_unavailable_formatter_output_is_not_a_lost_detection(self):
        common = dict(task_id=1, source='acw', detector='acw')
        rows = [dict(common, stage='before', status='ok', detected=True),
                dict(common, stage='ruff_default', status='preprocessing_error', detected=None),
                dict(common, stage='ruff_strict', status='ok', detected=False)]
        changes = transitions(rows)
        self.assertEqual(changes[0]['transition'], 'unavailable')
        self.assertIsNone(changes[0]['after_detected'])
        self.assertEqual(changes[1]['transition'], 'lost')


if __name__ == '__main__':
    unittest.main()
