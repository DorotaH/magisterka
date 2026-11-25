def max_distance(n, h, segments):
    # Initialize the maximum distance
    max_dist = 0

    # Iterate over all possible starting points
    for start in range(-10**9, 10**9 + 1):
        # Initialize the current position and height
        current_pos = start
        current_height = h

        # Iterate until the glider lands
        while current_height > 0:
            # Check if the current position is within any ascending airflow segment
            in_segment = False
            for x1, x2 in segments:
                if x1 <= current_pos < x2:
                    in_segment = True
                    break

            # Update the current position and height
            if in_segment:
                current_pos += 1
            else:
                current_pos += 1
                current_height -= 1

            # Update the maximum distance if the current position is greater
            if current_pos - start > max_dist:
                max_dist = current_pos - start

    # Return the maximum distance
    return max_dist

# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
h = int(data[1])
segments = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(n)]

# Call the function and print the result
print(max_distance(n, h, segments))
