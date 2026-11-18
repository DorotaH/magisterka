import random

n = int(input())

best = n

l = list(map(int, input().split()))
candidates = set()
candidates.add(2)


def gcd(x, y):
    while (y):
       x, y = y, x % y
    return x


def factAdd(n):
    for c in candidates:
        while n % c == 0:
            n //= c

    test = 3
    while test**2 <= n:
        while n % test == 0:
            candidates.add(test)
            n //= test
        test += 2
    if 1 < n:
        candidates.add(n)


for _ in range(100):
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)

    diff = [-1, 0, 1]

    for d1 in diff:
        a1 = d1 + l[a]
        if a1:
            for d2 in diff:
                a2 = d2 + l[b]
                if a2:
                    factAdd(gcd(a1, a2))

for cand in candidates:
    count = 0
    for v in l:
        if v <= cand:
            count += (cand - v)
        else:
            v2 = v % cand
            count += min(v2, cand - v2)
    if best > count:
        best = count
print(best)
