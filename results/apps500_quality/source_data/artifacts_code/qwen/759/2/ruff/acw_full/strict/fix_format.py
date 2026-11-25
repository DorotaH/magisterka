from sys import stdin

# Read input
hh, mm = map(int, stdin.readline().split())
H, D, C, N = map(int, stdin.readline().split())

# Calculate current time in minutes
current_time = hh * 60 + mm

# Calculate the time until 20:00
discount_time = 20 * 60

# Calculate the time until the cat is fed
feed_time = (H // D + 1) * D / 60

# Determine the optimal time to buy buns
if current_time + feed_time < discount_time:
    # Buy buns without discount
    buns_needed = H // N
    if H % N != 0:
        buns_needed += 1
    total_cost = buns_needed * C
else:
    # Buy buns with discount
    buns_needed = (H - (discount_time - current_time) * D) // N
    if (H - (discount_time - current_time) * D) % N != 0:
        buns_needed += 1
    total_cost = buns_needed * C * 0.8

# Output the result
print(f"{total_cost:.4f}")
