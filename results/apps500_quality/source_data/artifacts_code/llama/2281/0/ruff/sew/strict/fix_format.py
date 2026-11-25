n = int(input())
a = list(range(1, 1 + 2 * n))
a.sort()

print(*a[:n], *a[n:])
