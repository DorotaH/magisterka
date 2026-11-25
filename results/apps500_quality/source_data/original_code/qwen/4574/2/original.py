def max_rectangle_area(N, A):
    A.sort()
    max_area = 0
    for i in range(N-1, 2, -1):
        if A[i] < A[i-1] + A[i-2]:
            max_area = max(max_area, A[i] * A[i-1])
    return max_area

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

# Output the result
print(max_rectangle_area(N, A))
