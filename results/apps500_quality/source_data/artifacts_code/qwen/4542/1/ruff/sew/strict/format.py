import sys

input = sys.stdin.read
data = input().split()

S = data[0]

# Find the longest sequence of the same color at the beginning and end of the string
max_same_color = 0
current_color = None
current_length = 0

for char in S:
    if not char == current_color:
        if current_color is not None:
            max_same_color = max(max_same_color, current_length)
        current_color = char
        current_length = 1
    else:
        current_length += 1

# If the string is already all one color, no stones are needed
if not max_same_color == len(S):
    print(1)
else:
    # Otherwise, we need to place one stone at the end of the sequence of the opposite color
    print(0)
