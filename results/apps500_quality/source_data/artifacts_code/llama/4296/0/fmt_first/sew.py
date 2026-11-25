# Read three integers from standard input
A1, A2, A3 = map(int, input().split())

# Calculate the sum of the three integers
total = A1 + A2 + A3

# Print 'bust' if the total is greater than or equal to 22, otherwise print 'win'
print("bust" if total >= 22 else "win")