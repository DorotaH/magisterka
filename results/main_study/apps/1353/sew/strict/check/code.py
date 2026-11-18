"""
Codeforces Contest 266 Div 2 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""


def  main():
    n,m,a,b=read()
    if not b/m < a:
        print(n*a)
    else:
        if n%m and a * (n%m) > b:
            print((n//m + 1) * b)
        else:
            print((n%m) * a + (n//m) * b)

################################### NON-SOLUTION STUFF BELOW

def  read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs=input().strip()
    if  0 == mode: return  inputs
    if  1 == mode: return  inputs.split()
    if  2 == mode: return  list(map(int, inputs.split()))


def  write(s="\n"):
    if  s is  None: s = ""
    if  isinstance(s, list): s = " ".join(map(str, s))
    s=str(s)
    print(s, end="")

write(main())