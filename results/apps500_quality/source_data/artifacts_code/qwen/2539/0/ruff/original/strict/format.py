from math import gcd


def L(x, p):
    count = 0
    y = x + 1
    while True:
        if gcd(p, y) == 1:
            count += 1
            if count == k:
                return y
        y += 1


t = int(input())
results = []
for _ in range(t):
    x, p, k = map(int, input().split())
    results.append(L(x, p))

for result in results:
    print(result)
