import sys

# Read input
input = sys.stdin.read
data = input().split()

# Number of floors
n = int(data[0])

# Number of people on each floor
a = list(map(int, data[1:]))

# Function to calculate total electricity units for a given x


def calculate_electricity(x):
    return sum(2 * abs(i - x) * a[i] for i in range(n) if a[i] > 0)


# Find the minimum electricity units
min_electricity = float('inf')
for x in range(n):
    min_electricity = min(min_electricity, calculate_electricity(x))

# Print the result
print(min_electricity)
