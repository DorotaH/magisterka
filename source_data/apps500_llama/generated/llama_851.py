def can_solve(n, k, a):
    left, right = 0, n - 1
    count = 0
    while left <= right:
        if a[left] <= k:
            left += 1
            count += 1
        if a[right] <= k:
            right -= 1
            count += 1
        if left > right:
            break
    return count

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(can_solve(n, k, a))
