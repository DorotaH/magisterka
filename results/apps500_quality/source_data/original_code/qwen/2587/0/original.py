def find_min_x(n):
    # If n is 1, the only digit is 8 which gives the maximum possible r
    if n == 1:
        return 8
    # For n > 1, we need to construct the smallest number that gives the maximum possible r
    # The maximum r is obtained by constructing a number with the largest possible binary digits
    # The largest binary digit is 1, so we need to construct a number with the most 1s possible
    # The smallest number that gives the maximum possible r is 1 followed by (n-1) 9s
    return int('1' + '9' * (n - 1))

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Number of test cases
t = int(data[0])

# Process each test case
results = []
for i in range(1, t + 1):
    n = int(data[i])
    results.append(find_min_x(n))

# Print results
for result in results:
    print(result)
