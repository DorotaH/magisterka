def mini(arr, n, k):
    lo = [0 for _ in range(1 + n)]
    o = -1

    for i in range(n):
        if arr[i] == 1:
            o = i
        lo[i] = o
    a = 0
    i = 0
    while i < n:
        pos = lo[min(i + k - 1, n - 1)]
        if pos == -1 or k + pos <= i:
            return -1
        i = k + pos
        a += 1
    return a


n, k = list(map(int, input().split()))
arr = [int(i) for i in input().split()]
print(mini(arr, n, k))
