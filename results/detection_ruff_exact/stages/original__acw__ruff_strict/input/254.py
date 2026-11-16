import re


def words_ae(text):
    return re.findall(r"[ae]\w+", text)
