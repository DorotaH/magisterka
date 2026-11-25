def longest_streak(n, u):
	from collections import defaultdict

	max_streak = 0
	current_streak = 0
	count = defaultdict(int)
	color_count = defaultdict(int)
	last_seen = defaultdict(int)

	for i in range(n):
		if u[i] not in last_seen or last_seen[u[i]] + 1 == i:
			current_streak = i - last_seen[u[i]] + 1
		else:
			current_streak = i - last_seen[u[i]]

		if count[u[i]] == 0:
			color_count[u[i]] = 1
		else:
			color_count[u[i]] += 1

		count[u[i]] += 1
		last_seen[u[i]] = i

		if len(color_count) == 1:
			max_streak = max(max_streak, current_streak)
		else:
			for color in color_count:
				count[color] -= 1
				if count[color] == 0:
					del count[color]
					del color_count[color]
				else:
					color_count[color] -= 1
				current_streak -= 1
				max_streak = max(max_streak, current_streak)
				count[color] += 1
				color_count[color] += 1

	return max_streak


# Read input
n = int(input())
u = list(map(int, input().split()))

# Output the result
print(longest_streak(n, u))
