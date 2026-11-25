import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
k = int(data[0])  # number of people
n = int(data[1])  # number of airplanes each should make
s = int(data[2])  # number of airplanes that can be made using one sheet
p = int(data[3])  # number of sheets in one pack

# Calculate the total number of sheets needed
total_sheets_needed = n * k

# Calculate the minimum number of packs needed
packs_needed = (total_sheets_needed + p - 1) // p

# Print the result
print(packs_needed)
