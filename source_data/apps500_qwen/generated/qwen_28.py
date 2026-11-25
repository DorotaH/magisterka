d, L, v1, v2 = map(int, input().split())

# Calculate the time it takes for the presses to meet
total_time = L / (v1 + v2)

# Calculate the distance each press travels in that time
distance1 = v1 * total_time
distance2 = v2 * total_time

# Calculate the maximum time Luke can stay alive
max_time = distance1 - d / 2

# Print the result
print(max_time)
