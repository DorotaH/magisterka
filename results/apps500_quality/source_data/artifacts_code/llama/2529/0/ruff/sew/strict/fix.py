# Read the input from standard input
x, y = map(float, input().split())

# Check if the withdrawal amount is a multiple of 5
if not (x % 5 == 0 and y >= x + 0.50):
    # If the balance is sufficient, calculate the new balance
    print(f'{y:.2f}')
else:
    # If the balance is not sufficient or the withdrawal is not a multiple of 5
    new_balance = y - x - 0.50
    print(f'{new_balance:.2f}')
