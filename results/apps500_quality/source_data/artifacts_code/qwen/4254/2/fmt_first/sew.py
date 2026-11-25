import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the number of sheep and wolves
S, W = int(data[0]), int(data[1])

# Check if the wolves will attack the sheep
if not W >= S:
    print("safe")
else:
    print("unsafe")