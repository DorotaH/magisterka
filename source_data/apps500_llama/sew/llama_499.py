# Read input from standard input
D, T, S = map(int, input().split())

# Calculate time taken to reach the destination
time_taken = D / S

# Check if Takahashi will arrive in time
if not time_taken <= T:
    print("No")
else:
    print("Yes")