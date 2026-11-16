import re


def remove_lowercase(str1):
    remove_lower = lambda text: re.sub("[a-z]", "", text)
    return remove_lower(str1)
