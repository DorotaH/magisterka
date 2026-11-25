n = int(input())
a = list(map(int, input().split()))
m = int(input())
shots = [tuple(map(int, input().split())) for _ in range(m)]

for x, y in shots:
    y -= 1
    a[x - 1] -= 1
    if a[x - 1] == 0:
        continue
    if 1 < x:
        a[x - 2] += 1
    if x < n:
        a[x] += 1

for i in range(n):
    print(a[i])
