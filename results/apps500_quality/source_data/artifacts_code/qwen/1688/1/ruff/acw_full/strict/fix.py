

def count_tracks(n: int, a: list[int]) -> list[int]:
	result = [-1] * n
	for i in range(n):
		max_coolness = a[i]
		count = 1
		for j in range(1, n):
			next_track = (i + j) % n
			max_coolness = max(max_coolness, a[next_track])
			if a[next_track] < max_coolness // 2:
				break
			count += 1
		result[i] = count
	return result


# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Compute and print the result
result = count_tracks(n, a)
for r in result:
	print(r)
