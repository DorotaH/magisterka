def distribute_eggs(n, prices):
	total_a = 0
	total_g = 0
	g_count = 0

	for a, g in prices:
		total_a += a
		total_g += g
		if g < a:
			g_count += 1

	if abs(total_a - total_g) <= 500:
		result = ["A" if g < a else "G" for a, g in prices]
		return "".join(result)
	elif g_count > (1 + n) // 2:
		result = ["G"] * n
		for i in range(n):
			if total_g < total_a:
				result[i] = "A"
				total_a += 999 - prices[i][0]
				total_g -= prices[i][1]
		if abs(total_a - total_g) <= 500:
			return "".join(result)
	else:
		result = ["A"] * n
		for i in range(n):
			if total_g > total_a:
				result[i] = "G"
				total_g += 999 - prices[i][1]
				total_a -= prices[i][0]
		if abs(total_a - total_g) <= 500:
			return "".join(result)

	return "-1"


# Read input
n = int(input())
prices = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(distribute_eggs(n, prices))
