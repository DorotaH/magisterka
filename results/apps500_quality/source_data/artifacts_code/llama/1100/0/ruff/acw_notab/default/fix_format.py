import sys

n = int(sys.stdin.readline().strip())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


ans = sum((n - gcd(n, i)) // lcm(n, i) - 1 for i in range(1, n))
print(ans)
