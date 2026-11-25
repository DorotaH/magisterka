def min_turns_to_single_color(n, colors):
    # Find the number of connected components
    components = 0
    current_color = None
    for color in colors:
        if color != current_color:
            components += 1
            current_color=color
    
    # The minimum number of turns needed is the number of components minus one
    return max(0, components-1)

# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
colors = list(map(int, data[1:]))

# Output the result
print(min_turns_to_single_color(n, colors))
