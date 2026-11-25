import sys

# Read input from standard input
input_data = sys.stdin.read().split()

# Extract the withdrawal amount and initial balance
X, Y = int(input_data[0]), float(input_data[1])

# Check if the withdrawal amount is a multiple of 5
if not X % 5 != 0:
    if Y >= X + 0.50:
        new_balance = Y - X - 0.50
        print(f"{new_balance:.2f}")
    else:
        print(f"{Y:.2f}")
else:
    # Check if there are enough funds for the withdrawal including bank charges
    print(f"{Y:.2f}")