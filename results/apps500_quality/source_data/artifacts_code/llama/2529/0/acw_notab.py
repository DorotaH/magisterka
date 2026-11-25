# Read the input from standard input
x, y = map(float, input().split())

# Check if the withdrawal amount is a multiple of 5
if x % 5 == 0 and y >= 0.50 + x:
    # If the balance is sufficient, calculate the new balance
    new_balance = y - x - 0.50
    print('{:.2f}'.format(new_balance))
else:
    # If the balance is not sufficient or the withdrawal is not a multiple of 5
    print('{:.2f}'.format(y))
