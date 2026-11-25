def min_operations(s, t):
    n = len(s)
    m = len(t)
    a_count = s.count('a')
    b_count = s.count('b')
    a_index=0
    b_index = 0
    operations = []
    
    while a_count > 0 or b_count > 0:
        if a_count>0:
            a_index = a_index + 1
            a_count = a_count - 1
        if b_count>0:
            b_index = b_index + 1
            b_count = b_count - 1
        if a_index>0 and b_index>0:
            operations.append((a_index, b_index))
            a_count = a_count + b_index
            b_count = b_count + a_index
            a_index = b_index = 0
    
    return  len(operations), operations

# Read input
s, t = input().strip(), input().strip()

# Get the result
result=min_operations(s, t)

# Print the result
print(result[0])
for  op in  result[1]:
    print(op[0], op[1])