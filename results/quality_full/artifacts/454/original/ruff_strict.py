import re


def text_match_wordz(text):
    patterns = r"\w*z.\w*"
    if re.search(patterns, text):
        return "Found a match!"
    return "Not matched!"
