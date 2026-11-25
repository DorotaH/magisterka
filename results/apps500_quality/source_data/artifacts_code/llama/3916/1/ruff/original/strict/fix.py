import math


def get_prime_factors(n):
    factors = []
    i = 2
    while n > 1:
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
        if factors[0] == 2:
            path += 1
        else:
            path += len(factors)
        k = math.prod(factors)
    return path

def main():
    n = int(input())
    k = list(map(int, input().split()))

    node_to_path = {}
    for i in range(1, max(k) + 1):
        node_to_path[i] = get_path_length(i)

    for i in range(n):
        k[i] = node_to_path[k[i]]

    paths = {}
    for i in range(n):
        paths[k[i]] = paths.get(k[i], 0) + 1

    P = min(k)
    for node in sorted(node_to_path.keys(), key=lambda x: node_to_path[x], reverse=True):
        if node > P:
            P = node
            break

    total_path_length = 0
    for node in node_to_path:
        if node <= P:
            total_path_length += paths.get(node, 0) * node_to_path[node]
        else:
            total_path_length += paths.get(node, 0) * (node_to_path[node] + node_to_path[P])

    print(total_path_length)

if __name__ == "__main__":
    main()
