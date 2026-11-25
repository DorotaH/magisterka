n, m = map(int, input().split())
if m != n:
    a = m - 1
else:
    a = m + 1

if m == 1:
    a = 1

print(a)
