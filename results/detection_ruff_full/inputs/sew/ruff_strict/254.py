import re


def words_ae(text):
    list = re.findall(r"[ae]\w+", text)
    return list
