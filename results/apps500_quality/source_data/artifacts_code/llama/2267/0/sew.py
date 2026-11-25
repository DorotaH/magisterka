import  sys

n = int(sys.stdin.readline())
a = [sys.stdin.readline().strip() for _ in range(n)]

def  compare(a, b):
    """Compare two concatenated strings."""
    return  (a, b) if  a + b < b + a else (b, a)

# Sort the list of strings
a = sorted(a, key=compare)

# Concatenate the sorted list of strings
result = ''.join(a)

print(result)