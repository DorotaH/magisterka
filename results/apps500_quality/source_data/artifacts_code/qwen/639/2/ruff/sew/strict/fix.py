def min_operations(n, x, arr):
    current_mex = operations = 0

    while current_mex < x:
        if current_mex not in arr:
            operations += 1
            arr.add(current_mex)
        else:
            arr.remove(current_mex)
            operations += 1
        current_mex = current_mex + 1

    if x in arr:
        operations = operations + 1

    return  operations

# Read input
n, x = map(int, input().split())
arr = set(map(int, input().split()))

# Calculate and print the result
print(min_operations(n, x, arr))
