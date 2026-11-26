n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(0, m):
    x, y = map(int, input().split())
    y -= 1  # Convert to zero-indexed
    a[x - 1] -= 1
    if y > 0:
        a[x - 1] += a[x - 2]
        a[x - 2] = 0
    if y < a[x - 1]:
        a[x] += a[x - 1] - y
        a[x - 1] = y

for ai in a:
    print(ai)
