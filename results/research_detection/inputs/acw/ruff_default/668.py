import re


def replace(string, char):
    pattern = "{2,}" + char
    string = re.sub(pattern, char, string)
    return string
