import sys


def max_orders(n: int, k: int, a: int, b: int, q: int, updates: list[list[int]]) -> list[int]:
	# Initialize the production rate and the list to store the number of orders for each day
	current_production = b
	orders = [0] * n

	# Process the updates
	for update in updates:
		if update[0] == 1:
			day = update[1] - 1
			orders[day] += update[2]
		elif update[0] == 2:
			start_day = update[1] - 1
			end_day = start_day + k
			total_orders = sum(
				(
					min(orders[i], current_production)
					if i == start_day
					else min(orders[i], a)
				)
				for i in range(start_day, end_day)
			)
			# Print the result for the query
			print(total_orders)


# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
k = int(data[1])
a = int(data[2])
b = int(data[3])
q = int(data[4])
updates = []

# Read the updates
index = 5
for _ in range(q):
	update_type = int(data[index])
	if update_type == 1:
		day = int(data[1 + index])
		orders = int(data[2 + index])
		updates.append([update_type, day, orders])
		index += 3
	elif update_type == 2:
		start_day = int(data[1 + index])
		updates.append([update_type, start_day])
		index += 2

# Call the function and process the queries
max_orders(n, k, a, b, q, updates)
