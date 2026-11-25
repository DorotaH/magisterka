from collections import defaultdict
from heapq import heappop, heappush


def kth_order_statistic(n, s, m, k, a, segments):
	# Create a list to store the frequency of each element in the segments
	freq = [0] * (1 + n)

	# Create a dictionary to store the elements in each segment
	segment_elements = defaultdict(list)

	# Fill the frequency list and segment_elements dictionary
	for l, r in segments:
		for i in range(l - 1, r):
			freq[i] += 1
			heappush(segment_elements[i], a[i])

	k_elements = [heappop(segment_elements[i]) for i in range(n) if k <= freq[i]]
	# If there are fewer than k elements in the k_elements list, return -1
	return -1 if k > len(k_elements) else k_elements[k - 1]


# Read input
n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(s)]

# Print the result
print(kth_order_statistic(n, s, m, k, a, segments))
