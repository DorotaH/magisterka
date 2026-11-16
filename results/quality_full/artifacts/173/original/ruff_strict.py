import re


def remove_splchar(text):
    pattern = re.compile(r"[\W_]+")
    return pattern.sub("", text)
