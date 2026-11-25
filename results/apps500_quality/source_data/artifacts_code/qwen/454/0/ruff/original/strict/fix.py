
MOD = 10**9 + 7

def count_permutations(n, k):
    if k % 2 != n % 2:
        return 0

    def count_inversions(p):
        inversions = 0
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    inversions += 1
        return inversions

    def count_permutations_with_inversions(n, k):
        if k == 0:
            return 1
        if k % 2 != 0:
            return 0
        k //= 2
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(k, i - 1, -1):
                dp[j] = (dp[j] + dp[j - i]) % MOD
        return dp[k]

    return count_permutations_with_inversions(n, k)

n, k = map(int, input().split())
print(count_permutations(n, k))
