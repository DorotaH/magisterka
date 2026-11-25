N = int(input())
prices = [int(input()) for _ in range(N)]

# Sort the prices in descending order
prices.sort(reverse=True)

# Calculate the total amount with the discount
total = prices[0] // 2 + sum(prices[1:])

print(total)
