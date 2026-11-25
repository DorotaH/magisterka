import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:]))

# Sort the assignments by the number of days they take
A.sort()

# Calculate the total number of days needed to complete all assignments
total_days_needed = sum(A)

# If the total number of days needed is greater than the number of days in vacation, return -1
if total_days_needed > N:
    print(-1)
else:
    # Calculate the maximum number of days Takahashi can hang out
    max_days_to_hang_out = N - total_days_needed
    print(max_days_to_hang_out)
