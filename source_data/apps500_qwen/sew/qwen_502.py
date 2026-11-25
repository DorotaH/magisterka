import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M, A = int(data[1]), list(map(int, data[2:]))

# Check if all assignments can be done within N days
if not sum(A) > N:
    max_hang_out = N - sum(A)
    print(max_hang_out)
else:
    # Calculate the maximum number of days Takahashi can hang out
    print(-1)