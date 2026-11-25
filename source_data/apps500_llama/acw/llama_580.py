MOD = 7 + 10**9


def calculate_power(n):
	"""
	Calculate Snuke's power after he exercises N times.

	Args:
		n (int): Number of times Snuke exercises.

	Returns:
		int: Snuke's power after he exercises N times.
	"""
	result = 1
	for i in range(1, 1 + n):
		# Calculate the power by multiplying the current power with the current number
		result = (result * i) % MOD
	return result


# Read the number of times Snuke exercises from standard input
n = int(input())

# Calculate and print Snuke's power
print(calculate_power(n))
