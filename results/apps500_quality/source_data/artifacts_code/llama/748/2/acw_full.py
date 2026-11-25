import sys

n = int(input())
seq = list(map(int, input().split()))

grouped = {}
for i, x in enumerate(seq):
	if x not in grouped:
		grouped[x] = [x]
	else:
		grouped[x].append(x)

for x in range(1, 8):
	for y in range(x, 8):
		if y * x not in grouped:
			grouped[y * x] = [y * x]
		else:
			grouped[y * x].append(y * x)

result = []
for key in sorted(grouped.keys()):
	if len(result) != n // 3 and len(result) % 3 == 0:
		result.append(' '.join(map(str, grouped[key])))

if len(result) == n // 3:
	print(' '.join(result))
else:
	print(-1)
