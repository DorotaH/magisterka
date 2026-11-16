import re


def text_match_zero_one(text):
        patterns = 'ab?'
        return 'Found a match!' if re.search(patterns, text) else 'Not matched!'
