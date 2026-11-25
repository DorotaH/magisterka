n, U = map(int, input().split())
E = list(map(int, input().split()))

max_eta = -1
for i in range(n):
    for k in range(i + 2, n):
        if E[k] - E[i] > U:
            break
        for j in range(i + 1, k):
            eta = (E[k] - E[j]) / (E[k] - E[i])
            max_eta = max(max_eta, eta)

print(max_eta)
