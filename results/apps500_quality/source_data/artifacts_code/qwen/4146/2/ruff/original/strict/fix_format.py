import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
v = list(map(int, data[1:]))


# Function to find the minimum number of replacements needed to make the sequence /\/\/\/
def min_replacements_to_make_sequence_palindrome(v):
    if len(v) <= 2:
        return 0

    # Check the first two elements
    first = v[0]
    second = v[1]

    # If the sequence can be made by repeating the first element
    if all(x == first for x in v):
        return 0

    # If the sequence can be made by repeating the second element
    if all(x == second for x in v):
        return 0

    # If the sequence cannot be made by repeating any single element
    return 1


# Output the result
print(min_replacements_to_make_sequence_palindrome(v))
