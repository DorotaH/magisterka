# Read the number of items
n = int(input())

# Initialize the total cost
total_cost = 0

# Read and process each item price
for i in range(n):
    # Read the price of the item
    price = int(input())

    # If it's the last item, add its price to the total
    total_cost += price if i == n - 1 else price // 2
# Print the total cost
print(total_cost)
