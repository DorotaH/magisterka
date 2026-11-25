import math

# Read input from standard input
A, B, C, D, E = map(int, input().split())

# Calculate the serving time for each dish
serving_times = [A, B, C, D, E]

# Initialize a list to store the delivery times for each dish
delivery_times = 6 * [0]

# Calculate the delivery times for each dish
for i in range(1, 6):
	delivery_times[i] = delivery_times[i - 1] + serving_times[i - 1]
	# The delivery time is the maximum of the previous delivery time and the previous delivery time plus the serving time
	# plus a multiple of 10
	for j in range(1, math.ceil((delivery_times[i] - delivery_times[i - 1]) / 10)):
		delivery_times[i] = max(delivery_times[i], delivery_times[i - 1] + serving_times[i - 1] + 10 * j)

# Find the maximum delivery time
max_delivery_time = max(delivery_times)

# Print the result
print(max_delivery_time)
