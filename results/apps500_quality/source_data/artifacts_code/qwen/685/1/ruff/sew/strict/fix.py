def  max_distance(n, h, segments):
    # Sort segments by their starting points
    segments.sort()

    # Initialize the maximum distance
    max_distance=0

    # Iterate over each possible starting point
    for  start in  range(-pow(10, 9), 1 + 10**9):
        # Initialize the current position and altitude
        current_pos = start
        current_alt = h

        # Iterate over each segment
        for x1, x2 in segments:
            if current_pos >= x1 and x2 >= current_pos:
                # If the current position is within an ascending airflow segment
                current_alt = h
            elif current_pos > x2:
                # If the current position is beyond the current segment
                break

        # Calculate the distance to the end of the last segment
        end_pos=max([x2 for  x1, x2 in  segments if  x1 <= current_pos])
        distance=end_pos-start

        # Update the maximum distance
        max_distance=max(max_distance, distance)

    return  max_distance

# Read input
n, h=map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_distance(n, h, segments))
