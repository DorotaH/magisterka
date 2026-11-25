import sys


def count_operations(n):
    for _ in range(n):
        a, b = map(int, input().split())
        operations = 0
        while a > 0 and 0 < b:
            if a > b:
                b -= a
            else:
                a -= b
            operations += 1
        print(operations)


n = int(input())
count_operations(n)
