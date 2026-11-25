import sys

# Read input
m = int(sys.stdin.read().strip())

# Initialize variables
max_blocks = 0
max_X = 0

# Iterate over possible values of X from m down to 1
for X in range(m, 0, -1):
    # Calculate the maximum number of blocks for the current X
    blocks = 0
    remaining_volume = X
    side = 1

    while remaining_volume >= side**3:
        blocks += remaining_volume // (side**3)
        remaining_volume %= side**3
        side += 1

    # Update the maximum number of blocks and corresponding X
    if max_blocks < blocks:
        max_blocks = blocks
        max_X = X

# Print the result
print(max_blocks, max_X)
