"""
Codeforces Contest 266 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""

def main():
    n, m, a, b = read()
    if a > b / m:
        if n % m and a * (n % m) > b:
            print((1 + n // m) * b)
        else:
            print(a * (n % m) + b * (n // m))
    else:
        print(a * n)

################################### NON-SOLUTION STUFF BELOW

def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return list(map(int, inputs.split()))

def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

write(main())
