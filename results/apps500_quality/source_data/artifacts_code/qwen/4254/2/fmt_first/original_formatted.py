import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the number of sheep and wolves
S = int(data[0])
W = int(data[1])

# Check if the wolves will attack the sheep
if W >= S:
    print("unsafe")
else:
    print("safe")
