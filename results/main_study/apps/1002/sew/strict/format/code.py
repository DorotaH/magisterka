"""
Codeforces Round 251 Div 2 Problem A

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
n, d = read()
t = read()
s = sum(t) + 10 * n - 10
if not s > d:
    print((d - sum(t)) // 5)
else:
    print(-1)
