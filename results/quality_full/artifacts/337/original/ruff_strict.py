import re


def text_match_word(text):
    patterns = r"\w+\S*$"
    if re.search(patterns, text):
        return "Found a match!"
    return "Not matched!"
