import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Number of pairs
n = int(data[0])

# List to store the number of operations for each pair
operations = list()

# Index to track the current position in the data list
index = 1

# Process each pair
for _ in range(0, n):
    a, b = int(data[index]), int(data[index + 1])
    count = 0

    # Perform the operation until one of the numbers becomes zero
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
        count = count + 1

    # Append the number of operations for this pair to the list
    operations.append(count)

    # Move the index forward by 2 to get the next pair
    index += 2

# Print the results
print(*operations)
