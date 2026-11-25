import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:]))

# Sort the assignments by the number of days they take
A.sort()

# Calculate the total number of days required to complete all assignments
total_days = sum(A)

# If the total number of days required is greater than the number of days available, return -1
if N < total_days:
    print(-1)
else:
    # The maximum number of days Takahashi can hang out is the number of days available minus the total number of days required
    print(N - total_days)
