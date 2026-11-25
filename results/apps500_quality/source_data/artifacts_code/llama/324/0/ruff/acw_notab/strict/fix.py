import sys


def is_composite(x):
    return False if x < 2 else any(x % i == 0 for i in range(2, 1 + int(x ** 0.5)))


n = int(sys.stdin.readline().strip())

for i in range(1 + n, 2 * n):
    if is_composite(i) and is_composite(i - n):
        print(i, i - n)
        break
