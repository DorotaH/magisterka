import re


def remove_char(S):
    result = re.sub(r"[\W_]+", "", S)
    return result
