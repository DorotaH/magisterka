import re


def match(text):
    pattern = "[A-Z]+[a-z]+$"
    if re.search(pattern, text):
        return "Yes"
    return "No"
