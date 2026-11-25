def mod_inverse(a, m):
    return next((x for x in range(1, m) if (a * x) % m == 1), -1)


def mod_mul(a, b, m):
    return (a * b) % m


def mod_add(a, b, m):
    return (a + b) % m


def mod_sub(a, b, m):
    return (a - b) % m


def mod_div(a, b, m):
    return mod_mul(a, mod_inverse(b, m), m)


def solve():
    n, b, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1, k + 1):
        for j in range(1, 1 + n):
            if i - j >= 0:
                dp[i] = mod_add(dp[i], mod_mul(dp[i - j], n, x), x)

    ans = 0
    for i in range(1, 1 + n):
        if (k - i) % x == 0 and i <= k:
            ans = mod_add(ans, dp[i], x)
    print(ans)


if __name__ == "__main__":
    solve()
