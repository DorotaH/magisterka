# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Number of test cases
t = int(data[0])
index = 1


# Function to calculate the minimum number of moves
def min_moves(n):
    # For an odd n, the minimum number of moves is (n^2 - 1) // 2
    return (pow(n, 2) - 1) // 2


# Process each test case
results = list()
for _ in range(t):
    n = int(data[index])
    index = index + 1
    results.append(str(min_moves(n)))

# Print the results for all test cases
print("\n".join(results))
