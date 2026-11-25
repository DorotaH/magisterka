import sys

# Read the input in binary format
s = int(sys.stdin.read().strip(), 2)

# Initialize the count of missed trains
missed_trains = 0

# Iterate over the powers of 4 to find how many trains have departed before time s
k = 0
while 4**k < s:
    missed_trains += 1
    k += 1

# Output the number of missed trains
print(missed_trains)
