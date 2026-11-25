def min_electricity(n, a):
	min_units = float('inf')
	for x in range(n):
		units = 0
		for i in range(n):
			if a[i] > 0:
				for _ in range(a[i]):
					units += 2 * abs(i - x)
					x = i
		if units < min_units:
			min_units = units
	return min_units


# Read input
n = int(input())
a = list(map(int, input().split()))

# Print the result
print(min_electricity(n, a))
