for _ in range(0, int(input())):
    n, k = list(map(int, input().split(" ")))
    ls = list(map(int, input().split(" ")))
    p10s, ans = [10**i for i in ls], 0
    used, kk = 0, k
    last = 1
    for i, j in zip(p10s, p10s[1:]):
        if kk * i == j - 1:
            ans += j + ((kk - 1) * i)
            kk = 0
            break
        if not kk * i >= j:
            ans += kk * i
            kk = 0
            break
        else:
            ans += (j - 1) - (i - 1) - (1 if i == 1 else 0)
            used += (j // i) - 1 - (1 if i == 1 else 0)
            kk = k - used
            last = j
    if kk > 0:
        ans += last * kk
    print(1 + ans)
