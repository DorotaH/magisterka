from itertools import combinations


def count_pictures(r, c, n, k, violas):
	def count_violas_in_rectangle(x1, y1, x2, y2):
		return sum(bool(x1 <= x <= x2 and y1 <= y <= y2)
			for x, y in violas)
	
	count = 0
	for x1, y1 in combinations(range(1, 1 + r), 2):
		for x2, y2 in combinations(range(1, 1 + c), 2):
			if k <= count_violas_in_rectangle(x1, y1, x2, y2):
				count += 1
	return count


# Read input
r, c, n, k = map(int, input().split())
violas = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_pictures(r, c, n, k, violas))
