
def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

n, k = map(int, input().split())
A = list(map(int, input().split()))

def solve():
    """Compute the set of possible values of d"""
    ans = set()
    for a in A:
        for i in range(k):
            ans.add((a + i) % k)
    return ans

ans = solve()
print(len(ans))
print(*sorted(ans))
