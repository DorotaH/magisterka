# Read input from standard input
a = list(map(int, input().split()))

# Initialize the result
result = 0

# Iterate through the list and count the number of odd elements
for num in a:
    if  num % 2 != 0:
        result = result + 1

# Print the result to standard output
print(result)
