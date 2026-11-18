X, Y, Z, K = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)


ans = []
for i in range(X):
    if (i + 1) > K:
        break
    for j in range(Y):
        if (i + 1) * (1 + j) > K:
            break
        for k in range(Z):
            if (i + 1) * (1 + j) * (k + 1) > K:
                break
            ans.append(B[j] + A[i] + C[k])

ans.sort(reverse=True)

for i in range(K):
    print((ans[i]))
