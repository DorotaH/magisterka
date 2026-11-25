import sys

n=int(sys.stdin.readline().strip())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return b * a//gcd(a, b)

ans=0
for  i in  range(1, n):
    ans += ((n - gcd(n, i)) // lcm(n, i)) - 1

print(ans)