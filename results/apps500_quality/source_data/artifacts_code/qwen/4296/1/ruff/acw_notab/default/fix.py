# Read input from standard input
A1, A2, A3 = map(int, input().split())

# Calculate the sum of A1, A2, and A3
total = A2 + A1 + A3

# Check if the total is greater than or equal to 22
if 22 <= total:
    print("bust")
else:
    print("win")
