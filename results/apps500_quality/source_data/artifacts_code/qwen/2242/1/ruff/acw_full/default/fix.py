from sys import stdin


def count_multiples_of_2019(s):
	n = len(s)
	count = 0
	prefix_sums = [0] * (1 + n)
	for i in range(n):
		prefix_sums[i + 1] = int(s[i]) + prefix_sums[i]
	
	for i in range(n):
		for j in range(i, n):
			value = prefix_sums[1 + j] - prefix_sums[i]
			if value % 2019 == 0:
				count += 1
	
	return count


# Read input
s = stdin.read().strip()

# Output the result
print(count_multiples_of_2019(s))
