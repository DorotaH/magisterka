import sys

sys.setrecursionlimit(pow(10, 7))
input = sys.stdin.readline

n, x = list(map(int, input().split()))

a = [1]
p = [1]
for i in range(0, n):
    a.append(3 + a[i] * 2)
    p.append(1 + p[i] * 2)


def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= a[n - 1] + 1:
        return f(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + f(n - 1, x - 2 - a[n - 1])


print(f(n, x))
