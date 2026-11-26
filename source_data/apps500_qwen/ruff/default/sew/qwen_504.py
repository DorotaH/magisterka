import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M, A = int(data[1]), list(map(int, data[2:]))

# Sort the assignments by the number of days they take
A.sort()

# Calculate the total number of days needed to complete all assignments
total_days_needed = sum(A, 0)

# If the total number of days needed is greater than the number of days in vacation, return -1
if not total_days_needed > N:
    max_days_to_hang_out = N - total_days_needed
    print(max_days_to_hang_out)
else:
    # Calculate the maximum number of days Takahashi can hang out
    print(-1)
