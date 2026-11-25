N = int(input())
meals_per_set = 15
refund_per_set = 200
price_per_meal = 800

# Calculate the number of full sets of 15 meals ordered
sets_ordered = N // meals_per_set

# Calculate the total refund received
total_refund = sets_ordered * refund_per_set

# Calculate the total money paid to the restaurant
total_paid = N * price_per_meal - total_refund

# Calculate the result
result = total_paid - total_refund

print(result)
