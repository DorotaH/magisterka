import string
from collections import Counter


def valid(o):
    return all(abs(ord(x) - ord(y)) != 1 for x, y in zip(o, o[1:]))


def create(c, o):
    res = []
    for x in o:
        res.extend(x for _ in range(c[x]))
    return res


T = int(input())
for _ in range(T):
    c = Counter(input())
    o = []
    o1 = string.ascii_lowercase[1::2] + string.ascii_lowercase[::2]
    o2 = string.ascii_lowercase[1::2] + string.ascii_lowercase[::2]

    s1 = create(c, o1)
    s2 = create(c, o2)

    if valid(s1):
        print("".join(s1))
    elif valid(s2):
        print("".join(s2))
    else:
        print("No answer")
