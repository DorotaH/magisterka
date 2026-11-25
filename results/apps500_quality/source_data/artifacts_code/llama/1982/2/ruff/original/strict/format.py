import sys


def can_sum(n, k):
    if k > n:
        return "NO"
    if k == 1:
        return "YES" if n % 2 == 1 else "NO"
    sum_odd = 1
    count_odd = 1
    while sum_odd < n:
        sum_odd += 2
        count_odd += 1
    return "YES" if count_odd >= k else "NO"


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(can_sum(n, k))
