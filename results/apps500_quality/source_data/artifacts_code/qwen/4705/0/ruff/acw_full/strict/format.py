N = int(input())
meals_per_payment = 15
payment_return = 200

x = N * 800
y = payment_return * (N // meals_per_payment)

result = x - y
print(result)
