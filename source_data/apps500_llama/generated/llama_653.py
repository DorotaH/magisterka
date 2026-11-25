def check_reorder(n, m, a):
    total = 0
    for i in range(1, n + 1):
        sum_j = 0
        for j in range(i, n + 1):
            sum_j += a[j - 1] / j
        total += sum_j
        if total > m:
            return False
    return total == m

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if check_reorder(n, m, a):
        print("YES")
    else:
        print("NO")
