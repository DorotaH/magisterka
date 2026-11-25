import sys

input = sys.stdin.readline


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


n = read_int()
a = list(read_ints())

s = [0]
s.extend(s[-1] + a[i] for i in range(n))
mx = a[-1]
for i in range(n - 2, -1, -1):
    if a[i] >= a[i + 1]:
        a[i] = a[i + 1]

for i in range(n - 1):
    if a[i] >= a[i + 1]:
        a[i] = a[i]

for i in range(1, n):
    if a[i - 1] > a[i]:
        a[i] = a[i - 1]

for i in range(n):
    print(a[i], end=" ")
print()
