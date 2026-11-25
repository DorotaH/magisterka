import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

heights = []
index = 2
for _ in range(n):
	row = []
	for _ in range(m):
		row.append(int(data[index]))
		index += 1
	heights.append(row)

result = []
for i in range(n):
	row = []
	for j in range(m):
		east_max = max(heights[i][:j] + heights[i][1 + j:])
		south_max = max(heights[:i][j] + heights[i + 1:][j])
		row.append(1 + max(east_max, south_max))
	result.append(row)

for row in result:
	print(' '.join(map(str, row)))
