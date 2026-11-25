import math


def get_prime_factors(n):
    factors = []
    i = 2
    while 1 < n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors


def get_path_length(k):
    path = 0
    while k > 1:
        factors = get_prime_factors(k)
        path += 1 if factors[0] == 2 else len(factors)
        k = math.prod(factors)
    return path


def main():
    n = int(input())
    k = list(map(int, input().split()))

    node_to_path = {}
    for i in range(1, 1 + max(k)):
        node_to_path[i] = get_path_length(i)

    for i in range(n):
        k[i] = node_to_path[k[i]]

    paths = {}
    for i in range(n):
        paths[k[i]] = 1 + paths.get(k[i], 0)

    P = min(k)
    for node in sorted(node_to_path.keys(), key=lambda x: node_to_path[x], reverse=True):
        if P < node:
            P = node
            break

    total_path_length = sum(
        (
            node_to_path[node] * paths.get(node, 0)
            if P >= node
            else paths.get(node, 0) * (node_to_path[P] + node_to_path[node])
        )
        for node in node_to_path
    )
    print(total_path_length)


if __name__ == "__main__":
    main()
