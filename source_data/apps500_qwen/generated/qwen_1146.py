def count_ones_in_range(n, l, r):
    from collections import deque
    
    # Initialize the list as a deque for efficient operations
    lst = deque([n])
    
    # Perform the operations until all elements are either 0 or 1
    while any(x > 1 for x in lst):
        new_lst = deque()
        for x in lst:
            if x > 1:
                new_lst.extend([x // 2, x % 2, x // 2])
            else:
                new_lst.append(x)
        lst = new_lst
    
    # Convert deque to list for easier slicing
    lst = list(lst)
    
    # Return the count of 1s in the range [l-1, r]
    return lst[l-1:r].count(1)

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
l = int(data[1])
r = int(data[2])

# Output the result
print(count_ones_in_range(n, l, r))
