from sys import stdin, stdout


def can_make(k, coins):
    dp = [False] * (k + 1)
    dp[0] = True

    for c in coins:
        for i in range(k, c - 1, -1):
            if dp[i - c]:
                dp[i] = True

    return dp


def main():
    n, k = map(int, stdin.readline().split())
    coins = list(map(int, stdin.readline().split()))

    dp = can_make(k, coins)

    count = sum(bool(dp[i]) for i in range(k + 1))
    stdout.write("\n" + str(count))
    for i in range(k + 1):
        if dp[i]:
            stdout.write(str(i) + " ")


if __name__ == "__main__":
    main()
