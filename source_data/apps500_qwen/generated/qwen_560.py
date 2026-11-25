import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
H = int(data[0])
N = int(data[1])
A = list(map(int, data[2:]))

# Sort the moves in descending order
A.sort(reverse=True)

# Try to win the monster with the moves
for i in range(N):
    if H <= 0:
        print("Yes")
        exit()
    H -= A[i]

# If the loop completes without winning, print No
print("No")
