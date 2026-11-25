# Read the input from standard input
S, W = map(int, input().split())

# Check if the number of wolves is greater than or equal to that of sheep
if not W >= S:
    print("safe")
else:
    print("unsafe")