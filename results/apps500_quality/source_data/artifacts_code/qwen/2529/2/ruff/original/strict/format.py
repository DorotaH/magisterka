# Read input from standard input
X = int(input())
Y = float(input())

# Check if the withdrawal amount is a multiple of 5
if X % 5 == 0:
    # Check if there are enough funds in the account
    if Y >= X + 0.50:
        # Perform the withdrawal and subtract the bank charge
        Y -= X + 0.50
    else:
        # Insufficient funds, keep the current balance
        Y = Y

# Print the final account balance with two digits of precision
print(f"{Y:.2f}")
