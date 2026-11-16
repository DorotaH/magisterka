import re


def words_ae(text):
    return re.findall("[ae]\w+", text)
