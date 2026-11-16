import re


def text_match_wordz(text):
    patterns = r"\w*z.\w*"
    if not re.search(patterns, text):
        return "Not matched!"
    return "Found a match!"
