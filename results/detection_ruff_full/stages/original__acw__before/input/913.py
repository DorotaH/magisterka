import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    return bool(text.match(string))