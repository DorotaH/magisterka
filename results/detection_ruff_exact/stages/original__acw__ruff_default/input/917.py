import re


def text_uppercase_lowercase(text):
    patterns = "[A-Z]+[a-z]+$"
    return "Found a match!" if re.search(patterns, text) else "Not matched!"
