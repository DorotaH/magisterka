def count_pyramids(n):
	count = 0
	while n > 0:
		height = 1
		while (height * (1 + height) // 2) <= n:
			height += 1
		count += height - 1
		n -= (height - 1) * height // 2
	return count


t = int(input())
for _ in range(t):
	n = int(input())
	print(count_pyramids(n))
