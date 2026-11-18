import math
from collections import defaultdict
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))

    MAX = 1 + 10**7
    res = MAX * MAX

    #MAX_P = int(math.sqrt(MAX))
    MAX_P = 3163

    primes = []
    p = 2
    sieve = [True] * (MAX_P + 1)
    while MAX_P > p:
        if sieve[p]:
            primes.append(p)
            k = 2
            while k * p < MAX_P:
                sieve[k * p] = False
                k += 1
        p += 1

    np = len(primes)
    cand1 = {}
    cand2 = {}
    ind1 = {}
    ind2 = {}

    res = MAX * MAX
    for index in range(n):
        val = a[index]
        if val >= res:
            continue

        divisors = [1]
        p = 0
        while val > 0 and p < np:
            while val % primes[p] == 0:
                divisors += [primes[p] * d for d in divisors]
                val //= primes[p]
            p += 1
        if val > 1:
            divisors += [val * d for d in divisors]

        for d in set(divisors):
            if d not in cand1:
                cand1[d] = a[index]
                ind1[d] = index
            else:
                if (
                    d not in cand2
                    and a[index] < cand1[d]
                    or d in cand2
                    and a[index] < cand1[d]
                ):
                    cand2[d] = cand1[d]
                    ind2[d] = ind1[d]
                    cand1[d] = a[index]
                    ind1[d] = index
                elif d not in cand2 or a[index] < cand2[d]:
                    cand2[d] = a[index]
                    ind2[d] = index
                else:
                    continue
                if res > cand1[d] // d * cand2[d]:
                    x, y = ind1[d], ind2[d]
                    res = cand1[d] // d * cand2[d]

    print(min(1 + x, y + 1), max(1 + x, y + 1))


def __starting_point():
    main()

__starting_point()