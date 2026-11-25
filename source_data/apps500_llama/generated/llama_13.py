import sys

def is_composite(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False

n = int(sys.stdin.readline().strip())

for i in range(n + 1, 2 * n):
    if is_composite(i) and is_composite(i - n):
        print(i, i - n)
        break
