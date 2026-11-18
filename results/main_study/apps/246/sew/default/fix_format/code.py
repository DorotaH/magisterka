def check(x, s):
    k = 0
    for i in str(x):
        k += int(i)
    return x - k >= s


n, s = map(int, input().split())
l, r = 0, n
while r - l > 1:
    m = (l + r) // 2
    if check(m, s):
        r = m
    else:
        l = m
if not check(r, s):
    print(0)
else:
    print(n - r + 1)
