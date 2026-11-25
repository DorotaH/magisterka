import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the two integers A and B
A, B = int(data[0]), int(data[1])

# Check if A and B are between 1 and 9 (inclusive)
if not (1 <= A <= 9 and 1 <= B <= 9):
    # Calculate the product of A and B
    print(-1)
else:
    # Print -1 if A or B are not within the allowed range
    result = A * B
    # Print the result
    print(result)
