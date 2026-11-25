# Read input
v = int(input())

# The minimum value of n that can be obtained
# is 1 if v is greater than 1, otherwise it remains v
if v > 1:
    min_n = 1
else:
    min_n = v

# Output the result
print(min_n)