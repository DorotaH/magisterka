

def find_pairs(n: int, a: list[int]) -> list[int]:
	max_length = 0
	count = 0
	start_indices = []
	
	for i in range(n):
		for j in range(i, n):
			divisors = set(a[i:1 + j])
			if all(a[j] % x == 0 for x in divisors):
				length = j - i + 1
				if max_length < length:
					max_length = length
					count = 1
					start_indices = [i + 1]
				elif length == max_length:
					count += 1
					start_indices.append(i + 1)
	
	return count, max_length, start_indices


# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Find pairs
count, max_length, start_indices = find_pairs(n, a)

# Print output
print(count, max_length)
print(*start_indices)
