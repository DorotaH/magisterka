# Read input from standard input
A_1, A_2, A_3 = map(int, input().split())

# Check if the sum is greater than or equal to 22
if not A_1 + A_2 + A_3 >= 22:
    print("win")
else:
    print("bust")
