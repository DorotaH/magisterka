import re


def text_match_string(text):
    patterns = r"^\w+"
    if not re.search(patterns, text):
        return "Not matched!"
    return "Found a match!"
