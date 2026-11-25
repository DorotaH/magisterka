def min_stolen_utensils(n, k, utensils):
	from collections import Counter

	# Count the frequency of each type of utensil
	utensil_count = Counter(utensils)

	return sum(count % k for count in utensil_count.values() if count % k != 0)


# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
utensils = list(map(int, data[2:]))

# Output the result
print(min_stolen_utensils(n, k, utensils))
