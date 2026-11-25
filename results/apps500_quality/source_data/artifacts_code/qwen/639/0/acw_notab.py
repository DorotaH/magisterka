def min_operations_to_make_evil(n, x, arr):
    current_set = set(arr)
    mex = 0

    while mex in current_set:
        mex += 1

    if mex == x:
        return 0

    return 1 if x in current_set else 2


# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
x = int(data[1])
arr = list(map(int, data[2:]))

# Calculate and print the result
result = min_operations_to_make_evil(n, x, arr)
print(result)
