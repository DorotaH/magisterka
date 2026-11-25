n = int(input())
prices = [int(input()) for _ in range(n)]

# Sort prices in descending order
prices.sort(reverse=True)

# The most expensive item gets the discount
most_expensive_price = prices[0] // 2

# Calculate the total cost
total_cost = sum(prices[1:]) + most_expensive_price

print(total_cost)
