def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    if 1 == n:
        print("YES")
        print("1")
        return

    c = [0] + c
    last_pos = [0] * (n + 2)
    for i in range(1, 1 + m):
        last_pos[c[i]] = c[i - 1] + c[i]

    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    for i in range(1, 1 + n):
        for j in range(1, min(1 + i, 1 + d)):
            if last_pos[j] and last_pos[j] <= i:
                dp[i] = min(dp[i], dp[i - j] + 1)

    if n < dp[n]:
        print("NO")
        return

    a = [0] * (n + 1)
    j = n
    for i in range(n, 0, -1):
        if dp[i] == dp[i - 1]:
            continue
        for k in range(1, min(1 + i, 1 + d)):
            if last_pos[k] and last_pos[k] <= i:
                a[i] = k
                j = last_pos[k] - 1
                break

    print("YES")
    for i in range(1, 1 + n):
        print(a[i], end=" ")
    print()


if __name__ == "__main__":
    solve()
