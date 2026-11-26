from collections import defaultdict
import sys

input = sys.stdin.readline


def prime_factorization(n):
    fac = defaultdict(int)
    for i in range(2, 1 + int(n**0.5)):
        while n % i == 0:
            fac[i] += 1
            n = n // i
    if n > 1:
        fac[n] += 1
    return fac


def main():
    n, a = int(input()), list(map(int, input().split()))
    factors, pow2 = [prime_factorization(i) for i in a], [1]
    for _ in range(60):
        pow2.append(2 * pow2[-1] % 1000000007)

    dp = [0] * (1 + n)
    dp[0] = 1
    for i in range(1, 1 + n):
        dp[i] = 1
        for j in range(i):
            for k in range(i, 1 + j):
                if all(factors[j][fac] >= factors[k][fac] for fac in range(1, 60)):
                    dp[i] = (
                        dp[i]
                        + (dp[j] * pow2[factors[j][2] + factors[k][2]] % 1000000007)
                    ) % 1000000007
        dp[i] = (dp[i] - dp[i - 1]) % 1000000007
    print(dp[n])


main()
