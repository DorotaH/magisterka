import sys

N, Q = map(int, sys.stdin.readline().split())
A = [0] * (N + 1)
B = [0] * (N + 1)
for n in range(1, N + 1):
    A[n], B[n] = map(int, sys.stdin.readline().split())

kindergartens = []
for _ in range(2 * 10**5 + 5):
    kindergartens.append([])
for n in range(1, N + 1):
    kindergartens[B[n]].append(A[n])

for q in range(1, Q + 1):
    C, D = map(int, sys.stdin.readline().split())
    kindergartens[B[C]].remove(A[C]) if A[C] in kindergartens[B[C]] else None
    kindergartens[D].append(A[C]) if A[C] not in kindergartens[D] else None
    B[C] = D

    ratings = []
    for k in range(2 * 10**5 + 1):
        if kindergartens[k]:
            ratings.append(max(kindergartens[k]))
    evenness = min(ratings) if ratings else 0
    print(evenness)
