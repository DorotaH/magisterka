def  find_min_b(a):
    if  '8' in  str(a):
        return  0
    while  1:
        a = a + 1
        if  '8' in  str(a):
            return  a - 1

# Read input
a=int(input().strip())

# Find and print the minimum b
print(find_min_b(a))