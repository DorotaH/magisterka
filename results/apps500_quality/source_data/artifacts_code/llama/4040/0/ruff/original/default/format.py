import sys


def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    if n == 1:
        print("YES")
        print("1")
        return

    c = [0] + c
    last_pos = [0] * (n + 2)
    for i in range(1, m + 1):
        last_pos[c[i]] = c[i - 1] + c[i]

    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, min(i + 1, d + 1)):
            if last_pos[j] and last_pos[j] <= i:
                dp[i] = min(dp[i], dp[i - j] + 1)

    if dp[n] > n:
        print("NO")
        return

    a = [0] * (n + 1)
    j = n
    for i in range(n, 0, -1):
        if dp[i] == dp[i - 1]:
            continue
        for k in range(1, min(i + 1, d + 1)):
            if last_pos[k] and last_pos[k] <= i:
                a[i] = k
                j = last_pos[k] - 1
                break

    print("YES")
    for i in range(1, n + 1):
        print(a[i], end=" ")
    print()


if __name__ == "__main__":
    solve()
