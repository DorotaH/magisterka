# Read input from standard input
D, T, S = map(int, input().split())

# Calculate time taken to reach the destination
time_taken = D / S

# Check if Takahashi will arrive in time
if time_taken <= T:
    print("Yes")
else:
    print("No")
