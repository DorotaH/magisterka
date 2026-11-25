# Read input
n, k = map(int, input().split())
s = input()
t = input()

# Initialize the answer
c = 0

# Iterate over all possible prefixes
for i in range(1, n + 1):
    # Check if the prefix is within the range [s, t]
    prefix = s[:i]
    if  t >= prefix:
        c = c + 1

# Print the result
print(c)
