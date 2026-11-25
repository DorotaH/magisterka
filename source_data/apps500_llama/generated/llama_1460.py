from collections import defaultdict
import sys
input = sys.stdin.readline

def prime_factorization(n):
    fac = defaultdict(int)
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            fac[i] += 1
            n //= i
    if n > 1:
        fac[n] += 1
    return fac

def main():
    n = int(input())
    a = list(map(int, input().split()))
    factors = [prime_factorization(i) for i in a]
    pow2 = [1]
    for _ in range(60):
        pow2.append(2*pow2[-1] % 1000000007)

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = 1
        for j in range(i):
            for k in range(i, j + 1):
                if all(factors[j][fac] >= factors[k][fac] for fac in range(1, 60)):
                    dp[i] = (dp[i] + dp[j] * pow2[factors[j][2] + factors[k][2]] % 1000000007) % 1000000007
        dp[i] = (dp[i] - dp[i-1]) % 1000000007
    print(dp[n])

main()
