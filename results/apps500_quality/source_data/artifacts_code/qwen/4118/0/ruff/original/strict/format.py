import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the two integers A and B
A = int(data[0])
B = int(data[1])

# Check if A and B are between 1 and 9 (inclusive)
if 1 <= A <= 9 and 1 <= B <= 9:
    # Calculate the product of A and B
    result = A * B
    # Print the result
    print(result)
else:
    # Print -1 if A or B are not within the allowed range
    print(-1)
