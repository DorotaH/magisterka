def can(n, k):
    total = n
    s = 0

    while n > 0:
        cur = min(n, k)
        s += cur
        n -= cur

        n -= n // 10

    return s * 2 >= total


n = int(input())

le, rg = 0, n

while rg - le > 1:
    mid = (rg + le) // 2

    if can(n, mid):
        rg = mid
    else:
        le = mid

print(rg)
