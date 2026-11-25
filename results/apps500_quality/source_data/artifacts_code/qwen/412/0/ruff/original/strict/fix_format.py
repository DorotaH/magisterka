import sys

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
a = list(map(int, data[1:]))

# Initialize variables
max_power = 0
count = 0

# Iterate through the sequence to find the maximum power of 2 and count the numbers divisible by it
for num in a:
    power = 0
    while num % 2 == 0:
        num //= 2
        power += 1
    if power > max_power:
        max_power = power
        count = 1
    elif power == max_power:
        count += 1

# Output the result
print(max_power, count)
