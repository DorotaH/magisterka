def count_hexagons(n):
	return 6 * (2 * n**2 + 1)


n = int(input())
print(count_hexagons(n))
