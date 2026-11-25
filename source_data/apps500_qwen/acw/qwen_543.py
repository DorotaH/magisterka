N = int(input())
prices = [int(input()) for _ in range(N)]

# Sort the prices in descending order
prices.sort(reverse=True)

# Calculate the total amount with the discount
total = sum(prices[1:]) + prices[0] // 2

print(total)
