import re


def text_match_three(text):
    patterns = "ab{3}?"
    if not re.search(patterns, text):
        return "Not matched!"
    else:
        return "Found a match!"
