from  sys import  stdin

def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return (n, a)

def solve(n, a):
    inc = []
    dec = []
    prev = None
    inc_count = 0
    dec_count = 0
    is_increasing = True
    for  x in  a:
        if is_increasing and prev is not None and prev >= x:
            is_increasing=False
        if not is_increasing:
            dec.append(x)
            dec_count += 1
        else:
            inc.append(x)
            inc_count += 1
        prev = x

    if n == inc_count or n == dec_count:
        return  "NO"
    elif is_increasing:
        return "YES", inc_count, inc, dec_count, dec
    else:
        return  "YES", inc_count, inc, dec_count, dec

def print_output(inc_count, inc, dec_count, dec):
    if not inc_count == 0:
        print(inc_count)
        print(*inc)
    else:
        print("0")
    if not dec_count == 0:
        print(dec_count)
        print(*dec)
    else:
        print("0")

n, a=read_input()
result=solve(n, a)
if result[0] == "NO":
    print(result[0])
else:
    print_output(*result[1:])
