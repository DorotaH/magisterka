"""
Codeforces Contest 284 Div 1 Problem A

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def main():
    x1,y1 = read()
    x2,y2 = read()
    n, = read()
    ct = 0
    for _ in range(n):
        a,b,c = read()
        if (x1*a+b*y1+c)*(a*x2+y2*b+c) < 0: ct += 1
    print(ct)

#################################################### HELPERS



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