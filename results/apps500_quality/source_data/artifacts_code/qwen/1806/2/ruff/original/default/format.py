import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

intervals = []
for i in range(n):
    l = int(data[2 + 2 * i])
    r = int(data[3 + 2 * i])
    intervals.append((l, r))

queries = []
for i in range(m):
    x = int(data[2 + 2 * n + 2 * i])
    y = int(data[3 + 2 * n + 2 * i])
    queries.append((x, y))


def can_cover(x, y, intervals):
    covered = [False] * (y - x + 1)
    for l, r in intervals:
        for i in range(max(x, l), min(y, r) + 1):
            covered[i - x] = True
    return all(covered)


results = []
for x, y in queries:
    if can_cover(x, y, intervals):
        min_intervals = float("inf")
        for i in range(n):
            for j in range(i, n):
                if can_cover(x, y, intervals[i : j + 1]):
                    min_intervals = min(min_intervals, j - i + 1)
                    break
            if min_intervals < float("inf"):
                break
        results.append(min_intervals)
    else:
        results.append(-1)

for result in results:
    print(result)
