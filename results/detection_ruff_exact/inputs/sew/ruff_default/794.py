import re


def text_starta_endb(text):
    patterns = "a.*?b$"
    if not re.search(patterns, text):
        return "Not matched!"
    else:
        return "Found a match!"
