import re


def text_match_string(text):
    patterns = "^\w+"
    if not re.search(patterns, text):
        return "Not matched!"
    else:
        return "Found a match!"
