import heapq as hq


def heap_assending(nums):
	hq.heapify(nums)
	return [hq.heappop(nums) for _ in range(len(nums))]
