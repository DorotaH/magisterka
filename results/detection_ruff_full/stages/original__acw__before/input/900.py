import re
def match_num(string):
    text = re.compile(r"^5")
    return bool(text.match(string))