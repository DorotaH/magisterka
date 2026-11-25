def  max_pushes(n):
    return  n*(1 + n)//2

# Read input
n = int(input().strip())

# Calculate and print the result
print(max_pushes(n))
