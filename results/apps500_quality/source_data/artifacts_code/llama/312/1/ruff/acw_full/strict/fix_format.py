n, m = map(int, input().split())
a = m - 1 if m != n else 1 + m

if m == 1:
    a = 1

print(a)
