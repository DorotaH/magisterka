def  construct_string(n, s, t):
    if  t == s:
        return "NO"

    # Check if s and t can be avoided by repeating a pattern
    pattern = "abc" * n
    if  s in  pattern or  t in  pattern:
        return "NO"

    # Construct the result string
    res = ""
    for  i in  range(n):
        res+="abc"

    # Check if s and t are still in the result string
    if  s in  res or  t in  res:
        return "NO"

    return  "YES\n"+res

# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n, s = int(data[0]), data[1]
t = data[2]

# Get result
result = construct_string(n, s, t)

# Print result
print(result)
