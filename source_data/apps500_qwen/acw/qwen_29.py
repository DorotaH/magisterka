d, L, v1, v2 = map(int, input().split())

# Calculate the time it takes for the presses to meet
total_time = L / (v2 + v1)

# Calculate the maximum time Luke can stay alive
max_time = total_time - (d / (v2 + v1))

print(max_time)
