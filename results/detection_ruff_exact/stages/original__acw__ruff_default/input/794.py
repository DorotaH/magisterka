import re


def text_starta_endb(text):
    patterns = "a.*?b$"
    return "Found a match!" if re.search(patterns, text) else "Not matched!"
