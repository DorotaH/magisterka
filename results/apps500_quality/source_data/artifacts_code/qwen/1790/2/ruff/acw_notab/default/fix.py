

def possible_tram_lines(n: int, stops: list[list[int]]) -> list[int]:
    # Create a set to store the possible tram lines
    possible_lines = set()
    
    # Iterate through each stop
    for stop in stops:
        # If this is the first stop, initialize the possible lines
        if not possible_lines:
            possible_lines.update(stop)
        else:
            # Update the possible lines to the intersection with the current stop's lines
            possible_lines.intersection_update(stop)
    
    # Return the sorted list of possible tram lines
    return sorted(possible_lines)


# Read input
n = int(input())
stops = [list(map(int, input().split())) for _ in range(n)]

# Get the possible tram lines
result = possible_tram_lines(n, stops)

# Print the result
print(' '.join(map(str, result)))
