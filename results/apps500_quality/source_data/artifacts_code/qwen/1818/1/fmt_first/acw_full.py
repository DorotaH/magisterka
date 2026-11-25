from collections import defaultdict


def count_pairs(n, a):
	count = 0
	seen = defaultdict(int)

	for num in a:
		count += seen[num]
		x = num
		while 0 < x:
			if x % 2 == 0:
				x //= 2
			else:
				x -= 1
			count += seen[x]
		seen[num] += 1

	return count


# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(count_pairs(n, a))
