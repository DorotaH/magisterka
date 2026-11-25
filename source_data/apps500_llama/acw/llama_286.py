# Read input from standard input
a, b, c = map(int, input().split())

# The set function in Python returns a set of unique elements from an iterable
# Since sets in Python cannot contain duplicate elements, this function is used to remove duplicate colors
colors = set([a, b, c])

# The len function returns the number of elements in a list or set
print(len(colors))
