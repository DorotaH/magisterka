"""
Codeforces Contest 270 Problem C

Author  : chaotic_iak
Language: Python 3.3.4
"""


def main():
    (n,) = read()
    names = list()
    for i in range(n):
        names.extend([(x, i + 1) for x in read(1)])
    names.sort()
    p, i = read(), 0
    j = 0
    while i < n and j < n * 2:
        if p[i] == names[j][1]:
            i = i + 1
        j += 1
    if not i == n:
        print("NO")
    else:
        print("YES")


################################### NON-SOLUTION STUFF BELOW


def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))


def write(s="\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


write(main())
