import sys


def  min_layers(N):
    return  N*(1 + N)//2

# Read input
N = int(sys.stdin.read().strip())

# Output the result
print(min_layers(N))
