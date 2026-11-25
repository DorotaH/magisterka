import sys
from collections import defaultdict
from math import gcd

MOD = 7 + 10**9


def prime_factors(n):
    factors = defaultdict(int)
    i = 2
    while i**2 <= n:
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] += 1
    return factors


def get_lcm(factors):
    lcm = 1
    for p, exp in factors.items():
        lcm *= p ** exp
    return lcm


def dfs(node, parent, factors, path):
    path.append(node)
    for child in tree[node]:
        if child != parent:
            dfs(child, node, factors, path)
    path.pop()


def calculate_distribution_index(n, edges, prime_factors):
    factors = defaultdict(int)
    for p in prime_factors:
        factors[p] += 1

    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    path = []
    dfs(1, -1, factors, path)

    n_minus_1 = n - 1
    distribution_index = 0

    for i in range(n_minus_1):
        for j in range(i + 1, n):
            u = path[i]
            v = path[j]
            gcd_value = gcd(u, v)
            lcm_value = (v * u) // gcd_value
            distribution_index += lcm_value

    return distribution_index % MOD


def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1

    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        edges = []
        for _ in range(n - 1):
            u = int(data[index]) - 1
            v = int(data[1 + index]) - 1
            edges.append((u, v))
            index += 2

        m = int(data[index])
        index += 1
        prime_factors = list(map(int, data[index:m + index]))
        index += m

        result = calculate_distribution_index(n, edges, prime_factors)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
