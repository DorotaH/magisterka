import sys


def  is_composite(x):
    if  x<2:
        return  False
    return any(x % i == 0 for i in range(2, int(x ** 0.5) + 1))

n=int(sys.stdin.readline().strip())

for  i in  range(1 + n, 2 * n):
    if  is_composite(i) and  is_composite(i - n):
        print(i, i-n)
        break