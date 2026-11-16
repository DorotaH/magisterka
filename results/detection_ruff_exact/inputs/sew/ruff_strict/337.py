import re


def text_match_word(text):
    patterns = r"\w+\S*$"
    if not re.search(patterns, text):
        return "Not matched!"
    return "Found a match!"
