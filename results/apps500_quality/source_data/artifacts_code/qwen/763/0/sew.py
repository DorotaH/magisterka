import  sys

# Read input
input = sys.stdin.read
data = input().split()

# Number of floors
n = int(data[0])

# Number of people on each floor
a = list(map(int, data[1:]))

# Function to calculate total electricity units for a given x
def calculate_electricity(x):
    total=0
    for  i in  range(0, n):
        if  a[i]>0:
            total = total + abs(i - x) * 2 * a[i]
    return total

# Find the minimum electricity units
min_electricity = float('inf')
for x in range(n):
    min_electricity=min(min_electricity, calculate_electricity(x))

# Print the result
print(min_electricity)
