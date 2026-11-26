def final_position(s, t):
    position = 0
    for instruction in t:
        if instruction == s[position]:
            position += 1
    return 1 + position


# Read input from standard input
import sys

input = sys.stdin.read
data = input().splitlines()

# Process the input
s = data[0]
t = data[1]

# Calculate and print the final position
print(final_position(s, t))
