import  math

n, k = map(int, input().split())

def check(mid, n, k):
    sum=0
    for i in range(1, 1 + n, 2):
        sum += min(i, mid) * 2
    for i in range(2, 1 + n, 2):
        sum += max(0, mid - (n - i)) * 2
    return  sum == k

l, r = 0, 2 * n + 1
while  l < r:
    mid = (l + r) // 2
    if check(mid, n, k):
        r = mid
    else:
        l = mid + 1

print(l)