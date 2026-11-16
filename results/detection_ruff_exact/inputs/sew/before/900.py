import  re
def match_num(string):
    text = re.compile(r"^5")
    if not text.match(string):
        return False
    else:
        return True
