def f(n):
    m = 1 + int(n ** 0.5)
    t = [1] * (1 + n)
    for i in range(3, m):
        if t[i]: t[i * i :: i * 2] = [0] * ((n - i * i) // (i * 2) + 1)
    return [2] + [i for i in range(3, 1 + n, 2) if t[i]]


a, b, k = map(int, input().split())
n = 2000001

t, p, x = [-1] * n, f(n), -1
k -= 1; b += 1

for i in range(len(p) - k):
    t[p[i]] = p[i + k] - p[i]

t.reverse()
for i in range(1, n):
    if t[i] < 0: t[i] = 1 + t[i - 1]
t.reverse()

for i in range(a + 1, b):
    t[i] = max(t[i], t[i - 1])

for l in range(1, b - a + 1):
    if l > t[b - l]:
        x = l
        break
print(x)
