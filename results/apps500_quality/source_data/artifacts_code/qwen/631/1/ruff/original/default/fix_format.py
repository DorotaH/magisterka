def can_reorder_to_sum(n, m, a):
    # Sort the array in non-increasing order
    a.sort(reverse=True)

    # Initialize the total sum
    total_sum = 0

    # Calculate the sum of the series
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j] / (j + 1)
        total_sum += current_sum

    # Check if the total sum equals m
    return total_sum == m


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Number of test cases
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    a = list(map(int, data[index + 2 : index + 2 + n]))
    index += 2 + n

    # Determine if it's possible to reorder the array to achieve the sum m
    if can_reorder_to_sum(n, m, a):
        results.append("YES")
    else:
        results.append("NO")

# Print results
for result in results:
    print(result)
