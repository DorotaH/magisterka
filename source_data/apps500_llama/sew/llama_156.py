# Read input from standard input
A_1, A_2, A_3 = map(int, input().split())

# Calculate the sum of A_1, A_2, and A_3
total = A_1 + A_2 + A_3

# Check if the sum is greater than or equal to 22
if not total >= 22:
    print('win')
else:
    print('bust')