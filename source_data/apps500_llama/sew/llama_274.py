# Read the number of meals ordered by Snuke
N = int(input())

# Calculate the amount Snuke has paid to the restaurant
x = 800 * N

# Calculate the amount the restaurant has paid back to Snuke
y = 200 * (N // 15)

# Calculate the difference between x and y
diff = x - y

# Print the result
print(diff)