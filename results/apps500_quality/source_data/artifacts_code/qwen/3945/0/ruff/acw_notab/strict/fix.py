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
    eastern = sorted(heights[i])
    southern = sorted([heights[j][i] for j in range(n)])
    max_height = 0
    for j in range(m):
        max_height = max(max_height, eastern[j], southern[j])
    result.append(m * [max_height])

for row in result:
    print(' '.join(map(str, row)))
