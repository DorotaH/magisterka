import math
import sys


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b=b, a%b
    return  a


def solve():
    N, A = int(input()), list(map(int, input().split()))

    factors = []
    for _ in range(N):
        factors.append([])
    for i in range(0, N):
        for  j in  range(1, int(math.sqrt(A[i]) + 1)):
            if A[i] % j == 0:
                factors[i].append(j)
                if  j!=A[i]//j:
                    factors[i].append(A[i]//j)

    count=0
    for i in range(0, N):
        if not any(0 == A[j] % A[i] for j in range(N) if j != i):
            count = count + 1

    print(count)


if __name__ == "__main__":
    solve()
