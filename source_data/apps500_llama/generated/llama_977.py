import sys

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def read_str():
    return sys.stdin.readline().strip()

def write(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

n, p = read_ints()
a = read_ints()

def is_valid(x):
    if x < sum(a):
        return False
    if x == sum(a):
        return True
    permutation = [0] * (x + 1)
    for i in range(1, x + 1):
        permutation[i] = i
    for i in range(x, 0, -1):
        for j in range(1, n + 1):
            if i < a[j - 1]:
                permutation[i] = 0
                break
            if i == a[j - 1]:
                permutation[i] = j
    return permutation[x] != 0

def factorial(n):
    f = [1] * (n + 1)
    for i in range(2, n + 1):
        f[i] = f[i - 1] * i
    return f

def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 2:
        factors[n] = factors.get(n, 0) + 1
    return factors

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solve():
    total = 1
    for i in range(1, n + 1):
        total = total * (i * n - i + 1) // i
    total = total // factorial(n)
    good = 0
    result = []
    for x in range(sum(a) + 1, n * (n + 1) + 1):
        if is_valid(x):
            factors = prime_factors(x)
            is_good = True
            for factor in factors:
                if factor == p and factors[factor] % 2 == 0:
                    is_good = False
                    break
            if is_good:
                good += 1
                result.append(str(x))
    write(good)
    write(' '.join(result))

if __name__ == '__main__':
    solve()
