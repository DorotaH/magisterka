import re


def remove_extra_char(text1):
    pattern = re.compile(r"[\W_]+")
    return pattern.sub("", text1)
