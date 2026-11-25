import sys


def solve():
    n = int(input())
    total = n
    for i in range(1, n + 1):
        if 1 == i % 10:
            print(i - 1, 1)
        elif i % 10 == 2:
            print(1, i - 2)
        elif i % 10 == 3:
            print(i - 4, 1)
            print(i - 3, i - 1)
        elif i % 10 == 4:
            print(i - 5, i - 4)
            print(i - 4, i - 3)
            print(i - 3, i - 5)
            print(i - 2, i - 5)
        elif i % 10 == 6:
            print(i - 6, i - 4)
            print(i - 5, i - 6)
        elif i % 10 == 7:
            print(i - 7, i - 6)
            print(i - 6, i - 7)
            print(i - 5, i - 7)
            print(i - 7, i - 5)
            print(i - 6, i - 3)
        elif i % 10 == 8:
            print(i - 8, i - 7)
            print(i - 7, i - 8)
            print(i - 6, i - 8)
            print(i - 8, i - 6)
            print(i - 8, i - 4)
            print(i - 7, i - 4)
        elif i % 10 == 9:
            print(i - 9, i - 8)
            print(i - 8, i - 9)
            print(i - 9, i - 7)
            print(i - 8, i - 7)
            print(i - 9, i - 5)
            print(i - 8, i - 5)
            print(i - 7, i - 5)
        else:
            print(i - 1, i - 1)
            print(i - 1, i)
            print(i - 2, i)
            print(i - 2, i - 1)
            print(i - 2, i + 1)
            print(i - 1, i + 1)
            print(i, i + 1)
            print(i, i - 2)
            print(i, i)
            print(i + 1, i)
            print(i + 1, i - 2)
            print(i + 1, i - 1)
            print(i + 1, i)
    sys.stdout.flush()


solve()
