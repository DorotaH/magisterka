def max_sets(n, s):
	result = [0] * n
	for x in range(1, 1 + n):
		count = 0
		current_streak = 0
		for i in range(n):
			if s[i] != '?':
				if s[i] == '0':
					current_streak += 1
				else:
					current_streak = 1
				if current_streak >= x:
					count += 1
					current_streak = 0
			else:
				current_streak = 0
		result[x - 1] = count
	return result


# Read input
n = int(input().strip())
s = input().strip()

# Calculate and print the result
result = max_sets(n, s)
print(' '.join(map(str, result)))
