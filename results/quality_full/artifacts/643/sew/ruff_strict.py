import re


def text_match_wordz_middle(text):
    patterns = r"\Bz\B"
    if not re.search(patterns, text):
        return "Not matched!"
    return "Found a match!"
