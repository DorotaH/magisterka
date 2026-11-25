def can_sum(n, k):
    if k > n:
        return "NO"
    if k == 1:
        return "YES" if n % 2 == 1 else "NO"
    sum_odd = count_odd = 1
    while sum_odd < n:
        sum_odd += 2
        count_odd += 1
    return "YES" if k <= count_odd else "NO"


t = int(input())
for _ in range(0, t):
    n, k = map(int, input().split())
    print(can_sum(n, k))
