import re


def search_literal(pattern, text):
    match = re.search(pattern, text)
    s, e = match.start(), match.end()
    return (s, e)
