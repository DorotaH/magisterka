import sys

# Read input from standard input
L = int(sys.stdin.read().strip())

# Initialize the maximum volume
max_volume = 0

# Iterate over possible values of the first dimension
for x in range(1, L):
    # Iterate over possible values of the second dimension
    for  y in  range(1, L-x):
        # Calculate the third dimension
        z=L-x-y
        # Calculate the volume
        volume=y * x*z
        # Update the maximum volume if the current volume is greater
        if  volume > max_volume:
            max_volume=volume

# Print the maximum volume
print(max_volume)
