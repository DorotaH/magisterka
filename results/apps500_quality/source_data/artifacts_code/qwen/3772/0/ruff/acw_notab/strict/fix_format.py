def min_resistors(a, b):
    return b if a == 1 else min_resistors(b, a % b) + 1


# Read input
a, b = map(int, input().split())

# Output the result
print(min_resistors(a, b))
