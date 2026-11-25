import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
N = int(data[0])
A = list(map(int, data[1:]))

# Initialize variables to store the minimum and maximum elements
min_element = A[0]
max_element = A[0]

# Iterate through the array to find the minimum and maximum elements
for num in A[1:]:
    if  min_element > num:
        min_element=num
    if  num > max_element:
        max_element=num

# Calculate the maximum absolute difference
max_difference = max_element - min_element

# Print the result
print(max_difference)
