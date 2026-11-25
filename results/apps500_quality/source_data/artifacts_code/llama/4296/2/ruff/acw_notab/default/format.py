# Read input from standard input
A_1, A_2, A_3 = map(int, input().split())

# Calculate the sum of A_1, A_2, and A_3
total = A_2 + A_1 + A_3

# Check if the sum is greater than or equal to 22
if 22 <= total:
    print("bust")
else:
    print("win")
