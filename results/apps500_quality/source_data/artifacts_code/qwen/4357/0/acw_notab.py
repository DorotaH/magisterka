# Read input from standard input
A, B, C = map(int, input().split())

# Initialize the maximum allowance to 0
max_allowance = 0

# Iterate through all possible combinations of placing A, B, and C in the formula X + Y
for i in range(3):
    for j in range(3):
        if i != j:
            # Construct the two numbers by placing A, B, and C in all possible positions
            X = A * 10 + B if i == 0 else A * 10 + C if i == 1 else B * 10 + A if i == 2 else B * 10 + C if i == 3 else C * 10 + A if i == 4 else C * 10 + B
            Y = A * 10 + B if j == 0 else A * 10 + C if j == 1 else B * 10 + A if j == 2 else B * 10 + C if j == 3 else C * 10 + A if j == 4 else C * 10 + B
            # Calculate the allowance for this combination
            allowance = X + Y
            # Update the maximum allowance if this combination gives a higher value
            if max_allowance < allowance:
                max_allowance = allowance

# Print the maximum possible amount of the allowance
print(max_allowance)
