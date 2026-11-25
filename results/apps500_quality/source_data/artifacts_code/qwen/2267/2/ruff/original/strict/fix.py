from functools import cmp_to_key


def custom_sort(a, b):
    return (a + b) < (b + a)

def smallest_concatenation(strings):
    sorted_strings = sorted(strings, key=cmp_to_key(custom_sort))
    return ''.join(sorted_strings)

# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Get the smallest concatenation
result = smallest_concatenation(strings)

# Print the result
print(result)
