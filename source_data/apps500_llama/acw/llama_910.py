n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

colors = ['R', 'G', 'B']
color_indices = {}

for i in range(3):
	color = colors[i]
	for j in range(n):
		if flag[j][0] == color:
			color_indices[color] = (j, 0)
			break

for color in colors:
	if color not in color_indices:
		print("NO")
		break
else:
	for i in range(1, m):
		if color_indices[color][0] != color_indices['R'][0] or color_indices[color][1] != i:
			print("NO")
			break
	else:
		print("YES")
		break
else:
	print("NO")
