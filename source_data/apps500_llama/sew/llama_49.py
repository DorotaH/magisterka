N = int(input())

M = 0
for i in range(1, N + 1):
    P = (N + i) // 2
    if  i > P:
        P=N
    M += (i % P)

print(M)