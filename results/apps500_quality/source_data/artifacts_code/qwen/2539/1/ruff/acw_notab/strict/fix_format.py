from math import gcd


def kth_element(x, p, k):
    count = 0
    y = 1 + x
    while True:
        if gcd(p, y) == 1:
            count += 1
            if count == k:
                return y
        y += 1


t = int(input().strip())
results = []
for _ in range(t):
    x, p, k = map(int, input().strip().split())
    results.append(kth_element(x, p, k))

for result in results:
    print(result)
