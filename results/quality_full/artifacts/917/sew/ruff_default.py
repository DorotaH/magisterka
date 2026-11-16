import re


def text_uppercase_lowercase(text):
    patterns = "[A-Z]+[a-z]+$"
    if not re.search(patterns, text):
        return "Not matched!"
    else:
        return "Found a match!"
