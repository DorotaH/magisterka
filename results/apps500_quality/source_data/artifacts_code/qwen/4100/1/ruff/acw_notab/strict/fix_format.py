import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
Q = int(data[2])

scores = N * [K]
answers = data[3:]

for answer in answers:
    player = int(answer) - 1
    scores[player] -= 1
    for i in range(N):
        if i != player:
            scores[i] += 1

survivors = [player for player in range(N) if scores[player] > 0]

for i in range(N):
    if i in survivors:
        print("Yes")
    else:
        print("No")
