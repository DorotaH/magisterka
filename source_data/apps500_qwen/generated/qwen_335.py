# Read input
v = int(input())

# The minimum value of n that can be obtained
# is 1 if v is greater than 1, otherwise it remains v
min_n = 1 if v > 1 else v

# Output the result
print(min_n)
