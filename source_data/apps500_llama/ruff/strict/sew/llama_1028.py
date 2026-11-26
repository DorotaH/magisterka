import math
import sys


def main():
    n, x1, x2 = map(int, input().split())
    c = list(map(int, input().split()))

    possible = True
    for i in range(n):
        if x1 > c[i] * n or x2 > c[i] * n:
            possible = False
            break

    if not possible:
        print("No")
        return None

    c.sort(reverse=True)

    k1 = math.ceil(x1 / c[0])
    k2 = math.ceil(x2 / c[0])

    if n < k1 or n < k2:
        possible = False
    elif c[0] * k1 < x1 or c[0] * k2 < x2:
        possible = False

    if not possible:
        print("No")
        return None

    servers1 = [1]
    servers2 = [1]

    for i in range(1, n):
        if c[i] * k1 >= x1:
            servers1.append(i + 1)
            x1 -= c[i] * k1
        if c[i] * k2 >= x2:
            servers2.append(i + 1)
            x2 -= c[i] * k2

    if x1 or x2:
        possible = False

    if not possible:
        print("No")
    else:
        print("Yes")
        print(k1, k2)
        print(*servers1)
        print(*servers2)


if __name__ == "__main__":
    main()
