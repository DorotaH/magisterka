import sys

n = int(input())
w = list(map(int, input().split()))
s = input()

rows = [(i, w[i]) for i in range(n)]
rows.sort(key=lambda x: x[1])

ans = []
empty = []
occupied = {}
occupied_capacity = 0
for i in range(2 * n):
	if s[i] == "0":
		ans.append(1 + rows[0][0])
		empty.append(rows[0])
		occupied_capacity += 1
		occupied[rows[0][0]] = 1
		rows.pop(0)
		rows.sort(key=lambda x: x[1])
	else:
		if occupied_capacity > 0:
			index = min(occupied.keys())
			ans.append(1 + index)
			occupied[index] += 1
			occupied_capacity -= 1
		else:
			ans.append(1 + rows[-1][0])
			occupied[rows[-1][0]] = 1
			occupied_capacity += 1
			rows.pop(-1)

print(*ans)
