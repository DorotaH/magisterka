import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(sys.stdin.readline().strip())


def compare(a, b):
    """Compare two concatenated strings."""
    return (a, b) if a + b < b + a else (b, a)


# Sort the list of strings
a = sorted(a, key=lambda x: x if x else "", key=compare)

# Concatenate the sorted list of strings
result = "".join(a)

print(result)
