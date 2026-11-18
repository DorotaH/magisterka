"""
Codeforces Contest 281 Div 2 Problem D

Author  : chaotic_iak
Language: Python 3.3.4
"""


def main():
    (n,) = read()
    if not n % 2:
        print("white")
        print("1 2")
    else:
        print("black")


################################### NON-SOLUTION STUFF BELOW


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
