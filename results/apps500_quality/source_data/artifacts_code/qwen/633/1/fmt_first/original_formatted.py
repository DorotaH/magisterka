import math
from itertools import combinations


def gcd(a, b):
    return math.gcd(a, b)


def is_relatively_prime_graph(n, m):
    if m > n * (n - 1) // 2:
        return False
    if m == 0:
        return True

    # Create a list of edges that are relatively prime
    edges = []
    for v, u in combinations(range(1, n + 1), 2):
        if gcd(v, u) == 1:
            edges.append((v, u))

    # If there are not enough edges, return False
    if len(edges) < m:
        return False

    # Select m edges from the list of relatively prime edges
    selected_edges = edges[:m]

    # Check if the selected edges form a connected graph
    visited = set()
    stack = [1]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for u in [u for u, w in selected_edges if v == w]:
                if u not in visited:
                    stack.append(u)

    if len(visited) < n:
        return False

    return True


def construct_relatively_prime_graph(n, m):
    if not is_relatively_prime_graph(n, m):
        return "Impossible"

    # Create a list of edges that are relatively prime
    edges = []
    for v, u in combinations(range(1, n + 1), 2):
        if gcd(v, u) == 1:
            edges.append((v, u))

    # Select m edges from the list of relatively prime edges
    selected_edges = edges[:m]

    return "Possible\n" + "\n".join(f"{v} {u}" for v, u in selected_edges)


# Read input from standard input
n, m = map(int, input().split())

# Print the result
print(construct_relatively_prime_graph(n, m))
