import sys

# Read the input from standard input
S = sys.stdin.read().strip()

# Check if there is a pair of stations that will be connected by a bus service
if "AB" in S or "BA" in S:
    print("Yes")
else:
    print("No")
