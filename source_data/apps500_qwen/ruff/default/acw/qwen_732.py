def ice_cream_operations(n, x, operations):
    remaining_packs = x
    distressed_kids = 0

    for operation in operations:
        op_type, d = operation
        if op_type == "+":
            remaining_packs += d
        elif remaining_packs >= d:
            remaining_packs -= d
        else:
            distressed_kids += 1

    return remaining_packs, distressed_kids


# Read input
n, x = map(int, input().split())
operations = [input().split() for _ in range(n)]
operations = [(op[0], int(op[1])) for op in operations]

# Get the result
result = ice_cream_operations(n, x, operations)

# Print the result
print(result[0], result[1])
