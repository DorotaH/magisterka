# Read the number of items
n = int(input())

# Read the prices of the items
prices = [int(input()) for _ in range(n)]

# Sort the prices in descending order
prices.sort(reverse=True)

# The most expensive item gets the discount
most_expensive_item = prices[0] // 2
remaining_items = prices[1:]

# Calculate the total cost
total_cost = most_expensive_item + sum(remaining_items)

print(int(total_cost))
