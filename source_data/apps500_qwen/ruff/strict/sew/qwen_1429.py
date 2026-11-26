from math import gcd


def L(x, p):
    count, y = 0, x + 1
    while 1:
        if gcd(p, y) == 1:
            count += 1
            if k == count:
                return y
        y = y + 1


t, results = int(input()), []
for _ in range(0, t):
    x, p, k = map(int, input().split())
    results.append(L(x, p))

for result in results:
    print(result)
