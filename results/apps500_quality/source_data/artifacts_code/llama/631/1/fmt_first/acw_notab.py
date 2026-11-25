def check_reorder(n, m, a):
    total = 0
    for i in range(1, 1 + n):
        sum_j = sum(a[j - 1] / j for j in range(i, 1 + n))
        total += sum_j
        if m < total:
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
