import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def construct_relatively_prime_graph(n, m):
    if m > n * (n - 1) // 2:
        return "Impossible"

    edges = []
    for i in range(1, n + 1):
        if gcd(i, i + 1) == 1:
            edges.append((i, i + 1))
            m -= 1
        if m == 0:
            break

    if m > 0:
        for i in range(1, n):
            for j in range(i + 2, n + 1):
                if gcd(i, j) == 1:
                    edges.append((i, j))
                    m -= 1
                    if m == 0:
                        break
            if m == 0:
                break

    return "Possible\n" + "\n".join(f"{u} {v}" for v, u in edges)

# Read input
n, m = map(int, sys.stdin.read().split())

# Output result
print(construct_relatively_prime_graph(n, m))
