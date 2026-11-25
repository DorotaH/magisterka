def can_be_sum_of_distinct_odds(n, k):
    if k > n:
        return "NO"
    if k * 2 > n + 1:
        return "NO"
    if (n - k * (k + 1) // 2) % 2 == 0:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(can_be_sum_of_distinct_odds(n, k))
