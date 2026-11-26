from math import gcd


def kth_element(x, p, k):
    count, y = 0, x + 1
    while 1:
        if gcd(p, y) == 1:
            count += 1
            if k == count:
                return y
        y = y + 1


t, results = int(input().strip()), []
for _ in range(t):
    x, p, k = map(int, input().strip().split())
    results.append(kth_element(x, p, k))

for result in results:
    print(result)
