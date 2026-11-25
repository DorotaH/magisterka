import sys


def calculate_price(S):
    egg = 1 if S[0] == "o" else 0
    pork = 1 if S[1] == "o" else 0
    green_onions = 1 if S[2] == "o" else 0
    total_toppings = egg + pork + green_onions
    price = 700 + total_toppings * 100
    return price


S = input()
price = calculate_price(S)
print(price)
