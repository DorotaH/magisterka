import sys


def main():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [0] * n
    dp[1] = a[0]
    for i in range(2, n):
        dp[i] = a[i - 2] + dp[i - 1]
        for j in range(1, i - 1):
            dp[i] = min(dp[i], dp[j] + a[i - j - 1] + c + sum(b[k] for k in range(j, i - 1)))

    print(*dp)


if __name__ == "__main__":
    main()
