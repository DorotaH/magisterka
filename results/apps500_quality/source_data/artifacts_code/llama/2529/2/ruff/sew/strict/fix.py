# Read the input from standard input
X, Y = map(float, input().split())
bank_charge = 0.50

# Check if X is a multiple of 5 and if there are sufficient funds
if not (X % 5 == 0 and X <= Y):
    # Calculate the new balance after the transaction
    print(f"{Y:.2f}")
else:
    # If the transaction fails, print the current balance
    new_balance = Y - X - bank_charge
    print(f"{new_balance:.2f}")
