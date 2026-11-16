import re


def remove_char(S):
    return re.sub(r"[\W_]+", "", S)
