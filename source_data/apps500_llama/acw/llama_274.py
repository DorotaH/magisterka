# Read the number of meals ordered by Snuke
N = int(input())

# Calculate the amount Snuke has paid to the restaurant
x = N * 800

# Calculate the amount the restaurant has paid back to Snuke
y = (N // 15) * 200

# Calculate the difference between x and y
diff = x - y

# Print the result
print(diff)
