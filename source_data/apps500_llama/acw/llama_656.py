import math
import sys

hh, mm = map(int, input().split())
H, D, C, N = map(int, input().split())

# calculate minutes from midnight
minutes = hh * 60 + mm

# determine if the current time is after 20:00
discount = 1 if minutes >= 1200 else 0

# calculate the minimum number of buns to buy
buns_to_buy = math.ceil((H + (minutes * D)) / (N + (N * discount)))

# calculate the minimum amount of money to spend
min_cost = buns_to_buy * (C - (C * discount * discount))

# print the result to three decimal places
print(f"{min_cost:.4f}")
