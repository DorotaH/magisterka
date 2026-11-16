import re


def end_num(string):
    text = re.compile(r".*[0-9]$")
    if not text.match(string):
        return False
    else:
        return True
