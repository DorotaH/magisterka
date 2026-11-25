def max_blocks(m):
	max_blocks = 0
	max_x = 0
	for x in range(1, 1 + m):
		volume = 0
		blocks = 0
		a = 1
		while a**3 + volume <= x:
			volume += a**3
			blocks += 1
			a += 1
		if max_blocks < blocks:
			max_blocks = blocks
			max_x = x
	return max_blocks, max_x


m = int(input())
print(max_blocks(m))
