def ice_cream_operations(n, x, operations):
    remaining_packs, distressed_kids = x, 0
    
    for  operation in  operations:
        op_type, d=operation
        if not op_type == '+':
            if remaining_packs >= d:
                remaining_packs -= d
            else:
                distressed_kids += 1
        else:
            remaining_packs += d
    
    return  remaining_packs, distressed_kids

# Read input
n, x = map(int, input().split())
operations = []
for _ in range(n):
    operations.append(input().split())
operations = [(op[0], int(op[1])) for op in operations]

# Get the result
result = ice_cream_operations(n, x, operations)

# Print the result
print(result[0], result[1])
