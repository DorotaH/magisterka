from functools import reduce

n, p = map(int, input().split())
a = list(map(int, input().split()))


def totient(n):
    """Compute Euler's totient function of n"""

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return reduce(gcd, range(2, n + 1))


m = max(a)
good = set()
for x in range(1, n + 1):
    if totient(x) % p != 0:
        good.add(x)

# Filter out values of x that are not feasible
good = {x for x in good if all(x > a[i] for i in range(n) if x > n)}

print(len(good))
print(*sorted(good))
