"""
Codeforces Round 252 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""


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
        return [int(x) for x in inputs.split()]


def write(s="\n"):
    if isinstance(s, list):
        s = " ".join(s)
    s = str(s)
    print(s, end="")


################################################### SOLUTION
n, v = read()
a = []
for i in range(n):
    a.append(read())
a.sort(key=lambda x: x[0])
res = 0
for day in range(1, 3002):
    n = 0
    while a and a[0][0] <= day:
        if not a[0][1] <= v - n:
            a[0][1] -= v - n
            n = v
        else:
            n += a[0][1]
            a[0][1] = 0
        if not a[0][1] == 0:
            break
        else:
            a.pop(0)
    while a and a[0][0] == day - 1:
        a.pop(0)
    res += n
print(res)
