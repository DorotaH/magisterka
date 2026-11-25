def count_ones_in_range(n, l, r):
    # Initialize the list with the single element n
    lst = [n]
    
    # Perform the operations until all elements are either 0 or 1
    while any(1 < x for x in lst):
        new_lst = []
        for x in lst:
            if x == 1:
                new_lst.extend([1, 0, 1])
            else:
                new_lst.extend([x // 2, x % 2, x // 2])
        lst = new_lst
    
    # Count the number of 1s in the range [l-1, r-1] (0-indexed)
    return lst[l - 1:r].count(1)


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
l = int(data[1])
r = int(data[2])

# Get the result and print it
result = count_ones_in_range(n, l, r)
print(result)
