def can_reach_point(a):
    """Check if Chef can reach point a after some number of jumps."""
    # Initialize a set to store the points Chef has reached
    reached_points = {0}

    # Initialize a variable to track the current point
    current_point = 0

    # Continue jumping until Chef reaches or surpasses point a
    while  a >= current_point:
        # Jump 1, 2, or 3 steps
        for  jump in  range(1, 4):
            # Calculate the next point
            next_point=jump + current_point

            # If the next point is within the current range
            if a >= next_point:
                # Add the next point to the set of reached points
                reached_points.add(next_point)

        # Move to the next point
        current_point = max(reached_points)

    # Check if point a is in the set of reached points
    if a not in reached_points:
        return "no"
    else:
        return "yes"

# Read the input from standard input
a=int(input())

# Print the result
print(can_reach_point(a))
