"""
Codeforces Round 251 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""


def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs=input().strip()
    if 0 == mode:
        return inputs
    if 1 == mode:
        return inputs.split()
    if 2 == mode:
        return [int(x) for x in inputs.split()]


def write(s="\n"):
    if isinstance(s, list): s = " ".join(s)
    s=str(s)
    print(s, end="")

################################################### SOLUTION
n,x = read()
c = read()
c.sort()
print(sum(max(x - i,1) * c[i] for i in range(n)))