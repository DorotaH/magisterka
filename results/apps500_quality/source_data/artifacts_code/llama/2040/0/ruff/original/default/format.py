import sys

n = int(input())
b = []
for _ in range(n):
    b.append(int(input()))

a = []
for i in range(n):
    a.append("")
    num = b[i]
    while num > 0:
        a[i] = str(num % 9) + a[i]
        num //= 9

a = a[::-1]
a = a[1:] + ["1"] + a[:-1]
a = list(map(int, a))
print(*a)
