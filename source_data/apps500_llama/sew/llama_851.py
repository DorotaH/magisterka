def can_solve(n, k, a):
    left, right = 0, n - 1
    count = 0
    while left <= right:
        if k >= a[left]:
            left = left + 1
            count = count + 1
        if k >= a[right]:
            right = right - 1
            count = count + 1
        if left > right:
            break
    return  count

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(can_solve(n, k, a))
