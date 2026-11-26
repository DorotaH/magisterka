import math
import sys


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    factors = [[] for _ in range(N)]
    for i in range(N):
        for j in range(1, int(1 + math.sqrt(A[i]))):
            if A[i] % j == 0:
                factors[i].append(j)
                if j != A[i] // j:
                    factors[i].append(A[i] // j)

    count = sum(
        bool(all(A[j] % A[i] != 0 for j in range(N) if i != j)) for i in range(N)
    )
    print(count)


if __name__ == "__main__":
    solve()
