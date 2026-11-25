import  sys

N, K, Q = map(int, input().split())
A = []
for x in input().split():
    A.append(int(x) - 1)

score = [K] * N

for  a in  A:
    for  i in  range(0, N):
        if i != a:
            score[i] -= 1

for  i in  range(N):
    score[i] += Q - (N - 1)

for  i in  range(N):
    if score[i] <= 0:
        print("No")
    else:
        print("Yes")