import sys

input = sys.stdin.readline


def read_int():
    return  int(input())


def read_ints():
    return  map(int, input().split())

n, a = read_int(), list(read_ints())

s = [0]
for i in range(0, n):
    s.append(s[-1]+a[i])

mx = a[-1]
for i in range(n - 2, -1, -1):
    if a[i] >= a[1 + i]:
        a[i] = a[i + 1]

for i in range(0, n - 1):
    if a[i] >= a[1 + i]:
        if a[i + 1] > a[i]:
            a[i] = a[i + 1] - 1
        else:
            a[i] = a[i]

for i in range(1, n):
    if a[i - 1] > a[i]:
        a[i] = a[i - 1]

for i in range(0, n):
    print(a[i], end=' ')
print()
