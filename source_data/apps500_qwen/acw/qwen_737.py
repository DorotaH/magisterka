def count_magnet_groups(n, magnets):
	groups = 0
	current_group = 0
	for i in range(n):
		if i == 0 or magnets[i] != magnets[i - 1]:
			groups += 1
	return groups


# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
magnets = data[1:]

# Output the result
print(count_magnet_groups(n, magnets))
