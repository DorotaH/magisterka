from typing import List


def solve(n: int, m: int, intervals: List[List[int]], queries: List[List[int]]) -> List[int]:
	def can_cover(x: int, y: int) -> int:
		if y < x:
			return -1
		# Sort intervals by their right endpoint
		intervals.sort(key=lambda i: i[1])
		selected = []
		end = 0
		for l, r in intervals:
			if l > y:
				break
			if l > end:
				selected.append([l, r])
				end = r
		if end < x:
			return -1
		return len(selected)

	results = []
	for x, y in queries:
		results.append(can_cover(x, y))
	return results


# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
intervals = [[int(data[2 + i * 2]), int(data[3 + i * 2])] for i in range(n)]
queries = [[int(data[2 + 2 * n + i * 2]), int(data[3 + 2 * n + i * 2])] for i in range(m)]

# Solve and print results
results = solve(n, m, intervals, queries)
for result in results:
	print(result)
