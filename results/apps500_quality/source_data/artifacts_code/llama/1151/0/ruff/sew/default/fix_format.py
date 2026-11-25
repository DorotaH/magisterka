n, U = map(int, input().split())
E = list(map(int, input().split()))

max_eff = -1
for i in range(n - 2):
    for j in range(1 + i, n - 1):
        k = n - 1
        while j < k:
            if E[k] - E[i] <= U:
                max_eff = max(max_eff, (E[k] - E[j]) / (E[k] - E[i]))
                break
            k = k - 1

if not max_eff == -1:
    print(format(max_eff, ".12f"))
else:
    print(-1)
