import sys

input = sys.stdin.readline

N, K, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))

scores = [K] * (N + 1)
eliminated = set()

for q in range(1, Q + 1):
    player = A[q - 1]
    scores = [s - (N - 1) for s in scores]
    scores[player] += N - 1
    eliminated.update([i for i in range(1, N + 1) if scores[i] <= 0])

for i in range(1, N + 1):
    if i in eliminated:
        print("No")
    else:
        print("Yes")
