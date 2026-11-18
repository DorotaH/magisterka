"""
Codeforces Contest 288 Div 2 Problem C

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION


def main():
    m, t, r = read()
    w = read()
    if t < r:
        return -1
    covers = [0] * 1000
    ct = 0
    for i in w:
        x = covers[i]
        for j in range(r - x):
            for k in range(t):
                covers[i - j + k] += 1
            ct = ct + 1
    return ct


#################################################### HELPERS


def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if 0 == mode:
        return inputs
    if 1 == mode:
        return inputs.split()
    if 2 == mode:
        return list(map(int, inputs.split()))


def write(s="\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


write(main())
