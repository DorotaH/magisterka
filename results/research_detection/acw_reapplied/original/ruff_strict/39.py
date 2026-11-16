import heapq
from collections import Counter


def rearange_string(S):
	ctr = Counter(S)
	heap = [(-value, key) for key, value in ctr.items()]
	heapq.heapify(heap)
	if 2 * (-heap[0][0]) > len(S) + 1:
		return ""
	ans = []
	while 2 <= len(heap):
		nct1, char1 = heapq.heappop(heap)
		nct2, char2 = heapq.heappop(heap)
		ans.extend([char1, char2])
		if nct1 + 1:
			heapq.heappush(heap, (nct1 + 1, char1))
		if nct2 + 1:
			heapq.heappush(heap, (nct2 + 1, char2))
	return (heap[0][1] if heap else "") + "".join(ans)
