from collections import defaultdict

k, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_prefix_sum = [0]
a_prefix_sum.extend(a_prefix_sum[-1] + ai for ai in a)
b_to_index = {bi: i for i, bi in enumerate(sorted(b))}

min_score = min(a_prefix_sum[-1], min(b))
max_score = max(a_prefix_sum[-1], max(b))

min_score_diff = a_prefix_sum[-1] - min_score
max_score_diff = max_score - a_prefix_sum[-1]

min_score_possible = defaultdict(int)
max_score_possible = defaultdict(int)

for i, ai in enumerate(a_prefix_sum[:-1]):
	min_score_diff = min(min_score_diff, ai - a_prefix_sum[i])
	max_score_diff = max(max_score_diff, a_prefix_sum[-1] - ai)

	for j, bj in b_to_index.items():
		if a_prefix_sum[i] + j - min_score <= ai:
			min_score_possible[ai - min_score_diff] += 1
		if a_prefix_sum[i] + j + max_score_diff >= ai:
			max_score_possible[max_score_diff + ai] += 1

ans = max_score - min_score - (max(max_score_possible) - min_score_possible)
print(max(ans, 0))
