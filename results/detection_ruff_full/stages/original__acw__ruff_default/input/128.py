def long_words(n, str):
    txt = str.split(" ")
    return [x for x in txt if len(x) > n]
