import math
import sys

a, b, h, w, n = map(int, input().split())
arr = list(map(int, input().split()))


def min_extensions(a, b, h, w, arr):
    """Find the minimum number of extensions needed to reach the goal."""
    
    # Calculate the maximum number of times we can apply each extension to the length and width
    max_length = [math.ceil(a / x) for x in arr]
    max_width = [math.ceil(w / x) for x in arr]
    
    # Initialize the minimum number of extensions
    min_length = min(max_length)
    min_width = min(max_width)
    
    # Initialize the maximum number of extensions needed for the length and width
    max_length_needed = max(max_length)
    max_width_needed = max(max_width)
    
    # Check if we can place the rectangle on the field with all extensions
    if h >= min_length and min_width <= w:
        return 0
    
    for i in range(len(arr)):
        # Check if the current extension can help us place the rectangle on the field
        if max_length[i] <= h and max_width[i] <= w:
            # Update the minimum number of extensions
            min_length = min(min_length, max_length[i])
            min_width = min(min_width, max_width[i])
            
            # Update the maximum number of extensions needed
            max_length_needed = min(max_length_needed, max_length[i])
            max_width_needed = min(max_width_needed, max_width[i])
            
            # If we can place the rectangle on the field, return the minimum number of extensions
            if h >= min_length and min_width <= w:
                return i + 1
    
    # If we cannot place the rectangle on the field with all extensions, return -1
    return -1


# Print the minimum number of extensions
print(min_extensions(a, b, h, w, arr))
