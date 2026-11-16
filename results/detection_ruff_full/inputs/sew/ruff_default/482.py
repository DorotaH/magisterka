import re


def match(text):
    pattern = "[A-Z]+[a-z]+$"
    if not re.search(pattern, text):
        return "No"
    else:
        return "Yes"
