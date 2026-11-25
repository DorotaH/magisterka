import sys

# Read input from standard input
D, T, S = map(int, input().split())

# Calculate time it will take to reach the place
time_to_reach = D / S

# Check if Takahashi will arrive in time
if time_to_reach <= T:
	print("Yes")
else:
	print("No")
