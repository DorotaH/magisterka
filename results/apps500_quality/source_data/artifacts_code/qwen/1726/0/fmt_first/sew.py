import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
t = int(data[1])
a = list(map(int, data[2:]))

# Initialize variables
current_time = day = 0

# Iterate over each day
for i in range(n):
    # Add the work time for the current day
    current_time += a[i]
    # Check if the book can be finished today
    if  current_time >= t:
        day=1 + i
        break

# Print the result
print(day)