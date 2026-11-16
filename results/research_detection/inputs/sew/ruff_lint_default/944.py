import re


def num_position(text):
 for m in re.finditer(r"\d+", text):
    return  m.start()