import re


def text_match_two_three(text):
        patterns = 'ab{2,3}'
        return 'Found a match!' if re.search(patterns, text) else 'Not matched!'
