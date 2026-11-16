import re


def pass_validity(p):
    x = True
    while x:
        if (
            (len(p) < 6 or len(p) > 12)
            or not re.search("[a-z]", p)
            or not re.search("[0-9]", p)
            or not re.search("[A-Z]", p)
            or not re.search("[$#@]", p)
            or re.search(r"\s", p)
        ):
            break
        return True
        x = False
        break

    if x:
        return False
