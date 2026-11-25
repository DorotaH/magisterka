import math


def  reverse_hash(r):
    for  x in  range(1, 1 + int(math.sqrt(r))):
        y=(r-x**2-1)/(2 * x)
        if y==int(y) and y>0:
            return  f"{x} {int(y)}"
    return  "NO"

r=int(input())
print(reverse_hash(r))
