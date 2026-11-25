import sys

input = sys.stdin.read
data = input().split()

N, A = int(data[0]), list(map(int, data[1:]))

# Sort the array to minimize the total distance
A.sort()

# The minimum sadness will occur when b is the median of the array
# This is because the median minimizes the sum of absolute deviations
b = A[N // 2]

# Calculate the minimum possible sadness
min_sadness = sum(abs(A[i] - (b + i + 1)) for i in range(0, N))

print(min_sadness)