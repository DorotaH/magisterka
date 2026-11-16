import re


def text_match(text):
        patterns = 'ab*?'
        return 'Found a match!' if re.search(patterns,  text) else 'Not matched!'