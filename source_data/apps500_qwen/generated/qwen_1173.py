import sys

# Read input
input = sys.stdin.read
data = input().split()

n = int(data[0])
b = int(data[1])
a = int(data[2])
s = list(map(int, data[3:]))

# Initialize variables
current_b = b
current_a = a
max_segments = 0
i = 0

# Iterate through the segments
while i < n:
    if s[i] == 1:
        # If the segment is exposed to sunlight
        if current_b > 0:
            # Use battery
            current_b -= 1
            current_a += 1
            max_segments += 1
            i += 1
        elif current_a > 0:
            # Use accumulator
            current_a -= 1
            max_segments += 1
            i += 1
        else:
            break
    else:
        # If the segment is not exposed to sunlight
        if current_a > 0:
            # Use accumulator
            current_a -= 1
            max_segments += 1
            i += 1
        elif current_b > 0:
            # Use battery
            current_b -= 1
            current_a += 1
            max_segments += 1
            i += 1
        else:
            break

# Output the result
print(max_segments)
