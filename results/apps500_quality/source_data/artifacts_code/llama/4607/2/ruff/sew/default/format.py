import sys

# Read input from standard input
a, b = map(int, input().split())

# Initialize counter for Takahashi days
count = 0

# Iterate through each month
for month in range(1, a):
    # Check if the day is equal to the month
    if month == b:
        # Increment the counter
        count = count + 1

    # If the month is equal to 'a', break the loop
    if month == a:
        break

# Print the result
print(count)
