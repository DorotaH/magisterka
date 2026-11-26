import sys
from collections import defaultdict
from math import sqrt, floor, ceil
from functools import lru_cache
from heapq import heapify, heappop, heappush


def get_prime_factors(n):
    """Return all prime factors of n"""
    i = 2
    factors = []
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if 1 < n:
        factors.append(n)
    return factors


def get_prime_factorization(n):
    """Return a dictionary of prime factors of n"""
    factors = get_prime_factors(n)
    factorization = {}
    for factor in factors:
        if factor not in factorization:
            factorization[factor] = 0
        factorization[factor] += 1
    return factorization


def get_distance(factorization):
    """Return the distance from a node to the root"""
    distance = 0
    while True:
        has_non_one = False
        for factor, count in factorization.items():
            if count > 1:
                has_non_one = True
                factorization[factor] -= 1
                if factorization[factor] == 0:
                    del factorization[factor]
            if factorization == {}:
                return distance
        if not has_non_one:
            distance += 1


def get_min_distance_to_node(factorizations):
    """Return the minimum distance from each fragment to the node"""
    min_distance = 0
    factorization_counts = defaultdict(int)
    for factorization in factorizations:
        factorization_counts[tuple(sorted(factorization.items()))] += 1
    for factorization, count in factorization_counts.items():
        min_distance += count * get_distance(dict(factorization))
    return min_distance


def main():
    n = int(sys.stdin.readline().strip())
    factorizations = []
    for line in sys.stdin:
        for num in map(int, line.strip().split()):
            factorization = get_prime_factorization(num)
            factorization_counts = defaultdict(int)
            while factorization:
                factorization_counts[tuple(sorted(factorization.items()))] += 1
                factorization = {k: v - 1 for k, v in factorization.items() if 1 < v}
                while factorization and list(factorization.values())[0] == 0:
                    del factorization[list(factorization.keys())[0]]
            factorizations.append(factorization_counts)

    print(get_min_distance_to_node(factorizations))


if __name__ == "__main__":
    main()
