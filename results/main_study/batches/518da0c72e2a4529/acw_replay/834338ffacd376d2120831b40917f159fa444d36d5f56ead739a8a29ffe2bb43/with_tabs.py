class Solution:
	def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
		edges = []
		for i, (begin, end) in enumerate(intervals):
			edges.extend(((begin, -float("inf"), i), (end, -begin, i)))
		edges = sorted(edges)
		open_intervals = {}
		ints = []
		for first, second, index in edges:
			print(first, second, open_intervals)
			if second == -float("inf"):
				open_intervals[index] = 2
				continue

			for i in range(open_intervals.get(index, 0)):
				ints.append(first - i)
				for j in list(open_intervals):
					if intervals[j][0] <= ints[-1]:
						open_intervals[j] -= 1
						if open_intervals[j] <= 0:
							del open_intervals[j]
		print(ints)
		return len(ints)
