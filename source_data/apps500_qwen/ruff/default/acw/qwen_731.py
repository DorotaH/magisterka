def ice_cream_management(n, x, operations):
    ice_cream = x
    distressed_kids = 0

    for operation in operations:
        op, d = operation
        if op == "+":
            ice_cream += d
        elif op == "-":
            if ice_cream >= d:
                ice_cream -= d
            else:
                distressed_kids += 1

    return ice_cream, distressed_kids


# Read input
n, x = map(int, input().split())
operations = [input().split() for _ in range(n)]

# Process operations and print result
result = ice_cream_management(n, x, operations)
print(result[0], result[1])
