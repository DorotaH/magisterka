import sys

input = sys.stdin.read
data = input().split()

N, A = int(data[0]), list(map(int, data[1:]))

# If the number of stones in the first pile is even, Takahashi can always win by moving 1 stone to the second pile
if not A[0] % 2 == 0:
    print(-1)
else:
    # If the number of stones in the first pile is odd, Aoki can always win by removing 1 stone from the first pile
    print(1)
