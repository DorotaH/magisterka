N = int(input())
meals_per_payment, payment_return = 15, 200

x, y = N * 800, (N // meals_per_payment) * payment_return

result = x - y
print(result)