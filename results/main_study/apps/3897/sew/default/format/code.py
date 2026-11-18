from collections import defaultdict

m = 1_000_000_007

f = [0] * 15001
f[0] = 1
for i in range(1, 15001):
    f[i] = (i * f[i - 1]) % m


def c(n, k):
    return (f[n] * pow((f[n - k] * f[k]) % m, m - 2, m)) % m


def prime(n):
    m, t = int(n**0.5) + 1, [1] * (n + 1)
    for i in range(3, m):
        if t[i]:
            t[i * i :: 2 * i] = [0] * (1 + (n - i * i) // (2 * i))
    return [2] + [i for i in range(3, 1 + n, 2) if t[i]]


p, s = prime(31650), defaultdict(int)


def g(n):
    for j in p:
        while n % j == 0:
            n //= j
            s[j] += 1
        if j * j > n:
            s[n] += 1
            break


n, a = int(input()) - 1, list(map(int, input().split()))

for i in a:
    g(i)
if 1 in s:
    s.pop(1)

d = 1
for k in list(s.values()):
    d = (d * c(k + n, n)) % m
print(d)
