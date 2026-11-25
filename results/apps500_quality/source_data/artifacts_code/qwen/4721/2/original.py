import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

# The number of blocks is (n-1) * (m-1)
print((n-1) * (m-1))
