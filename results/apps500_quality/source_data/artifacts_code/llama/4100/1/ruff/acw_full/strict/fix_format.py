N, K, Q = map(int, input().split())
A = [int(x) - 1 for x in input().split()]

score = N * [K]

for a in A:
    for i in range(N):
        if i != a:
            score[i] -= 1

for i in range(N):
    score[i] += Q - (N - 1)

for i in range(N):
    if score[i] <= 0:
        print("No")
    else:
        print("Yes")
