import sys

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
p = int(data[1])
m = int(data[2])
topups = [(int(data[3 + i * 2]), int(data[4 + i * 2])) for i in range(n)]

# Initialize variables
current_balance = 0
topup_index = 0
days_with_negative_balance = 0

# Iterate through each day
for day in range(1, 1 + m):
    # Check if there is a topup on this day
    while topup_index < n and topups[topup_index][0] == day:
        current_balance += topups[topup_index][1]
        topup_index += 1

    # Deduct the daily payment
    current_balance -= p

    # Check if the balance is negative
    if 0 > current_balance:
        days_with_negative_balance += 1

# Output the result
print(days_with_negative_balance)
