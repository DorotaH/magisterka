N = int(input())

M = 0
for i in range(1, N + 1):
    P = (N + i) // 2
    if P < i:
        P = N
    M += i % P

print(M)
