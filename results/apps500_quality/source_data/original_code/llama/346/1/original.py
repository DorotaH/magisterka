from functools import cache

def max_points(n, m, a, b):
    @cache
    def dp(i, j, k):
        if i == n: return 0
        if j == 0: return max(0, dp(i + 1, 0, k))
        if k == 0: return max(0, dp(i + 1, 1, a[i] if i + 1 in b else 0))
        max_points_with_auction = max(0, dp(i + 1, 1, max(k - a[i], a[i])) + a[i])
        max_points_without_auction = dp(i + 1, 0, k)
        return max(max_points_with_auction, max_points_without_auction)

    return max(0, dp(0, 0, 0)) + a[0]

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_points(n, m, a, b))
