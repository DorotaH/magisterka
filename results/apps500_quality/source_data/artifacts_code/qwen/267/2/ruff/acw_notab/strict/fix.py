MOD = 998244353


def count_numbers_with_k_digits(n, k):
    if k == 1:
        return n
    if k == 10:
        return n * (1 + n) // 2
    dp = [[0] * 11 for _ in range(2)]
    dp[0][0] = 1
    for i in range(1, 1 + n):
        for j in range(1, 11):
            dp[i % 2][j] = (dp[(i - 1) % 2][j - 1] + (10 - j) * dp[(i - 1) % 2][j]) % MOD
    return dp[n % 2][k]


def sum_of_numbers_with_k_digits(l, r, k):
    return (count_numbers_with_k_digits(r, k) - count_numbers_with_k_digits(l - 1, k) + MOD) % MOD


def main():
    l, r, k = map(int, input().split())
    result = sum_of_numbers_with_k_digits(l, r, k)
    print(result)


if __name__ == "__main__":
    main()
