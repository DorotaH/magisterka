from collections import defaultdict


def max_occurrences(nums):
	dict = defaultdict(int)
	for i in nums:
		dict[i] += 1
	return max(dict.items(), key=lambda x: x[1])
