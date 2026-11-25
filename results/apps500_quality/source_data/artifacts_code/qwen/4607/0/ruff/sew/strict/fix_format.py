import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the month and day from the input
a = int(data[0])
b = int(data[1])

# Initialize the count of Takahashi days
takahashi_count = 0

# Iterate over all possible days from 2018-1-1 to 2018-a-b
for month in range(1, 1 + a):
    for day in range(1, 1 + min(b, month)):
        if month == day:
            takahashi_count += 1

# Print the total number of Takahashi days
print(takahashi_count)
