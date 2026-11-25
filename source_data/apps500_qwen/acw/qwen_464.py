import sys

# Read input from standard input
input_data = sys.stdin.read().split()

# Extract the withdrawal amount and initial balance
X = int(input_data[0])
Y = float(input_data[1])

# Check if the withdrawal amount is a multiple of 5
if X % 5 == 0 and Y >= 0.50 + X:
	new_balance = Y - X - 0.50
	print(f"{new_balance:.2f}")
else:
	print(f"{Y:.2f}")
