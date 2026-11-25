def can_be_represented(n, k):
    if k > n // 2:
        return False
    sum_odd = 1
    count_odd = 1
    while sum_odd < n:
        sum_odd += 2 * count_odd + 1
        count_odd += 1
    return count_odd >= k


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if can_be_represented(n, k):
        print("YES")
    else:
        print("NO")
