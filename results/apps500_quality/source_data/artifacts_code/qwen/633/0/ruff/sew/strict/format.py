from math import gcd


def is_relatively_prime_graph(n, m):
    if m != n - 1:
        return "Impossible"

    edges = list()
    for i in range(1, 1 + n):
        for j in range(i + 1, n + 1):
            if 1 == gcd(i, j):
                edges.append((i, j))
                if len(edges) == m:
                    return "Possible\n" + "\n".join(f"{a} {b}" for a, b in edges)
    return "Impossible"


# Read input
n, m = map(int, input().split())

# Output result
print(is_relatively_prime_graph(n, m))
