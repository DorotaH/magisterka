import sys


def read_ints():
    return list(map(int, input().split()))


k, n = read_ints()
a, b = read_ints(), read_ints()

min_score, max_score = min(b), max(b)

min_score_diff, max_score_diff = min(a), max(a)

min_score -= sum(a[: k - n], 0)
max_score -= sum(a[: k - n], 0)

min_score = max(min_score, 0)
max_score = min(max_score, 4000000)

print(max_score - min_score + 1)
