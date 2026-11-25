
def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the least common multiple of a and b"""
    return a * b // gcd(a, b)

n = int(input())
a = list(map(int, input().split()))

min_lcm = float('inf')
i, j = 0, 0
for i in range(n - 1):
    for j in range(i + 1, n):
        current_lcm = lcm(a[i], a[j])
        min_lcm = min(min_lcm, current_lcm)

print(i + 1, j + 1)
