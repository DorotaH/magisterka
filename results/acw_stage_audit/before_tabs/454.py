import re


def text_match_wordz(text):
        patterns = '\w*z.\w*'
        return 'Found a match!' if re.search(patterns, text) else 'Not matched!'
