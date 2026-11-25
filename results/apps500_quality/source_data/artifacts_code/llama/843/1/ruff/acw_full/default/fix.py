n = int(input())
directions = input()
lengths = list(map(int, input().split()))

position = 0
visited = set()

while position < n:
	if position in visited:
		print("INFINITE")
		break
	visited.add(position)
	if directions[position] == '>':
		position += lengths[position]
	else:
		position -= lengths[position]
else:
	print("FINITE")
