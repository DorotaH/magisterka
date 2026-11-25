import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M, A = int(data[1]), list(map(int, data[2:]))

# Sort the assignments by the number of days they take
A.sort()

# Calculate the total number of days required to complete all assignments
total_days = sum(A, 0)

# If the total number of days required is greater than the number of days available, return -1
if not total_days > N:
    print(N - total_days)
else:
    # The maximum number of days Takahashi can hang out is the number of days available minus the total number of days required
    print(-1)
