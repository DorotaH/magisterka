import  sys

input=sys.stdin.read
data=input().split()

n, m = int(data[0]), int(data[1])

intervals=list()
for  i in  range(n):
    l, r = int(data[2 + 2 * i]), int(data[3 + 2 * i])
    intervals.append((l, r))

queries=list()
for  i in  range(m):
    x, y = int(data[2 + 2 * n + 2 * i]), int(data[3 + 2 * n + 2 * i])
    queries.append((x, y))


def  can_cover(x, y, intervals):
    covered = [False] * (y - x + 1)
    for l, r in intervals:
        for  i in  range(max(x, l), min(y, r) + 1):
            covered[i - x] = True
    return all(covered)

results=list()
for  x, y in  queries:
    if not can_cover(x, y, intervals):
        results.append(-1)
    else:
        min_intervals = float('inf')
        for i in range(n):
            for j in range(i, n):
                if can_cover(x, y, intervals[i:j+1]):
                    min_intervals = min(min_intervals, j - i + 1)
                    break
            if min_intervals < float('inf'):
                break
        results.append(min_intervals)

for  result in  results:
    print(result)
