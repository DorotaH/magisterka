import sys


def read_ints():
	return list(map(int, input().split()))


k, n = read_ints()
a = read_ints()
b = read_ints()

min_score = min(b)
max_score = max(b)

min_score_diff = min(a)
max_score_diff = max(a)

min_score -= sum(a[:k - n])
max_score -= sum(a[:k - n])

min_score = max(min_score, 0)
max_score = min(max_score, 4000000)

print(max_score - min_score + 1)
