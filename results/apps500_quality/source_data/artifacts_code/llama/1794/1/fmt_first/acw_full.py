def sum_of_pairs(n, a):
	"""
	Compute the sum of all values ρ_{i}, j among all pairs 1 ≤ i < j ≤ n.

	Args:
		n (int): The number of stations.
		a (list): A list of integers, where a[i] represents the maximum station that can be reached from station i + 1.

	Returns:
		int: The sum of all values ρ_{i}, j among all pairs 1 ≤ i < j ≤ n.
	"""

	# Initialize a list to store the minimum number of tickets needed to reach each station
	d = [float("inf")] * (1 + n)

	# The minimum number of tickets needed to reach the first station is 0
	d[1] = 0

	# Iterate over the list of allowed stations
	for i in range(1, n):
		# For each station, update the minimum number of tickets needed to reach the next stations
		for j in range(i + 1, min(a[i - 1], 1 + n)):
			d[j] = min(d[j], d[i] + 1)

	# Compute the sum of all values ρ_{i}, j among all pairs 1 ≤ i < j ≤ n
	return sum((d[n] - d[i]) * (n - i) for i in range(1, n))


# Read the number of stations from the input
n = int(input())

# Read the list of allowed stations from the input
a = list(map(int, input().split())) + [1]

# Print the sum of all values ρ_{i}, j among all pairs 1 ≤ i < j ≤ n
print(sum_of_pairs(n, a))
