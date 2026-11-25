A, B, T = map(int, input().split())
total_biscuits = 0
i = 1
while i * A <= T + 0.5:
	total_biscuits += B * (i % 2)
	i += 1
print(total_biscuits)
