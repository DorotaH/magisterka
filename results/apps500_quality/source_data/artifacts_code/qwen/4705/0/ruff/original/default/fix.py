N = int(input())
meals_per_payment = 15
payment_return = 200

x = N * 800
y = (N // meals_per_payment) * payment_return

result = x - y
print(result)
