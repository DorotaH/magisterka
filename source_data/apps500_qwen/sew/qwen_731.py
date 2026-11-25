def ice_cream_management(n, x, operations):
    ice_cream, distressed_kids = x, 0
    
    for  operation in  operations:
        op, d=operation
        if  op == '+':
            ice_cream+=d
        elif  op=='-':
            if not ice_cream >= d:
                distressed_kids += 1
            else:
                ice_cream -= d
    
    return  ice_cream, distressed_kids

# Read input
n, x = map(int, input().split())
operations = []
for _ in range(n):
    operations.append(input().split())

# Process operations and print result
result = ice_cream_management(n, x, operations)
print(result[0], result[1])
