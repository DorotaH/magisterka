n, U = map(int, input().split())
E = list(map(int, input().split()))

max_eff = -1
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        k = n - 1
        while k > j:
            if E[k] - E[i] <= U:
                max_eff = max(max_eff, (E[k] - E[j]) / (E[k] - E[i]))
                break
            k -= 1

if max_eff == -1:
    print(-1)
else:
    print(format(max_eff, ".12f"))
