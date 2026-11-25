import math


def min_path_sum(n, k):
	# Calculate the factorial of each k_i
	factorials = [math.factorial(k_i) for k_i in k]
	
	# Initialize a dictionary to store the minimum path to each node
	min_path = {1: 0}
	
	# Function to get the minimum path to a node
	def get_min_path(node):
		if node in min_path:
			return min_path[node]
		min_path[node] = get_min_path(node // get_lowest_prime_divisor(node)) + 1
		return min_path[node]
	
	# Function to get the lowest prime divisor of a number
	def get_lowest_prime_divisor(n):
		if n % 2 == 0:
			return 2
		for i in range(3, int(math.sqrt(n)) + 1, 2):
			if n % i == 0:
				return i
		return n
	
	# Calculate the total minimum path sum
	total_min_path = sum(get_min_path(factorial) for factorial in factorials)
	
	return total_min_path


# Read input
n = int(input().strip())
k = list(map(int, input().strip().split()))

# Calculate and print the result
print(min_path_sum(n, k))
