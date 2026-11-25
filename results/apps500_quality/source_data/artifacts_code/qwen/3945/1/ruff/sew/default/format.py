import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

heights = []
index = 2
for i in range(n):
    row = list()
    for j in range(m):
        row.append(int(data[index]))
        index = index + 1
    heights.append(row)

result = []
for i in range(n):
    row = list()
    for j in range(m):
        east_max, south_max = (
            max(heights[i][:j] + heights[i][j + 1 :]),
            max(heights[:i][j] + heights[i + 1 :][j]),
        )
        row.append(max(east_max, south_max) + 1)
    result.append(row)

for row in result:
    print(" ".join(map(str, row)))
