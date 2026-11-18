"""
Codeforces Contest 266 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""


def ceildiv(a,b):
    return  a//b+(1 if  a%b else 0)


def main():
    n,a,b = read()
    s = n*6
    if b*a>=s:
        print(a*b)
        print(a,b)
        return None
    t = int((6*n) ** .5)
    tgt = 9001*n
    tgta = 0
    tgtb = 0
    for i in range(1, 1+t):
        c=ceildiv(s,i)
        if i >= a and c >= b:
            if tgt > i*c:
                tgt, tgta = i*c, i
                tgtb = c
        if i >= b and c >= a:
            if tgt > i*c:
                tgt, tgtb = i*c, i
                tgta = c
    print(tgt)
    print(tgta,tgtb)

################################### NON-SOLUTION STUFF BELOW

def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if 0 == mode: return inputs
    if 1 == mode: return inputs.split()
    if 2 == mode: return list(map(int, inputs.split()))


def write(s="\n"):
    if s is None: s=""
    if isinstance(s, list): s=" ".join(map(str, s))
    s = str(s)
    print(s, end="")

write(main())