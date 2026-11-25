def final_position(s, t):
    position = 0
    for instruction in t:
        if s[position] == instruction:
            position += 1
    return position + 1

# Read input from standard input
import sys
input = sys.stdin.read
data = input().splitlines()

# Process the input
s = data[0]
t = data[1]

# Calculate and print the final position
print(final_position(s, t))
