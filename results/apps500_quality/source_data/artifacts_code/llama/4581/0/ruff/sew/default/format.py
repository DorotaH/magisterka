S = input()
price, toppings = 700, 0

if S[0] == "o":
    toppings = toppings + 1
if S[1] == "o":
    toppings = toppings + 1
if S[2] == "o":
    toppings = toppings + 1

print(price + (toppings * 100))
