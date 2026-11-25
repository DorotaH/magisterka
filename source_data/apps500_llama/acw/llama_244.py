S = input()
price = 700
toppings = 0

if S[0] == 'o':
	toppings += 1
if S[1] == 'o':
	toppings += 1
if S[2] == 'o':
	toppings += 1

print(price + 100 * toppings)
