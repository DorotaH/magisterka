# Read input from standard input
a = list(map(int, input().split()))

# Initialize the result
result = 0

# Iterate through the list and count the number of odd elements
for num in a:
    if  0 != num % 2:
        result = result + 1

# Print the result to standard output
print(result)