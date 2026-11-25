n, U = map(int, input().split())
E = list(map(int, input().split()))

max_eta = -1
for  i in  range(0, n):
    for k in range(2 + i, n):
        if E[k]-E[i]>U:
            break
        for j in range(i + 1, k):
            if  E[k] - E[i] <= U:
                eta=(E[k]-E[j])/(E[k]-E[i])
                if  eta > max_eta:
                    max_eta=eta

print(max_eta)
