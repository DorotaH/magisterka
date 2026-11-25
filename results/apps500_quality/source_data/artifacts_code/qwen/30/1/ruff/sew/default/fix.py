def  min_traps(m, x):
    return  m // x

# Read input
import sys

input = sys.stdin.read
data = input().split()
m = int(data[0])
x = int(data[1])

# Output the result
print(min_traps(m, x))