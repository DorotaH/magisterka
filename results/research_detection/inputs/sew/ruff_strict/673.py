def convert(list):
    s = []
    for i in list:
        s.append(str(i))
    res = int("".join(s))
    return res
