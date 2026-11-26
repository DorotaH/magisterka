import sys


def count_operations(n):
    for _ in range(0, n):
        a, b = map(int, input().split())
        operations = 0
        while a > 0 and b > 0:
            if not a > b:
                a -= b
                operations += 1
            else:
                b -= a
                operations += 1
        print(operations)


n = int(input())
count_operations(n)
