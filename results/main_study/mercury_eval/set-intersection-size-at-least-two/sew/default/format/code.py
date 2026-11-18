class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        edges = list()
        for i, (begin, end) in enumerate(intervals, 0):
            edges.append((begin, -float("inf"), i))
            edges.append((end, -begin, i))
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
                    if ints[-1] >= intervals[j][0]:
                        open_intervals[j] -= 1
                        if open_intervals[j] <= 0:
                            del open_intervals[j]
        print(ints)
        return len(ints)
