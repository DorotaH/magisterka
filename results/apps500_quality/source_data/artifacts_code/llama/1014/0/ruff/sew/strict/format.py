import math

n = int(input())


def check(x, y):
    return "white" if (1 == x and y == n) else "black"


if n % 2 == 0:
    print("black")
else:
    print("white")
    if n == 2:
        print("1 2")
    else:
        print(f"{int(n / 2)} {n}")
