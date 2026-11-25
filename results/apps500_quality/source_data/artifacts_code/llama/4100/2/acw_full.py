import sys

N, K, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

scores = N * [K]
for a in A:
	for i in range(N):
		if i + 1 != a:
			scores[i - 1] -= 1

	min_score = min(scores)
	if min_score <= 0:
		scores = [score - min_score for score in scores]

for i in range(N):
	if scores[i - 1] > 0:
		print('Yes')
	else:
		print('No')
