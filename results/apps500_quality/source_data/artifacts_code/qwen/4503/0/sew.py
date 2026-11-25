import sys
input = sys.stdin.read
data = input().split()

H = int(data[0])
N = int(data[1])
A = list(map(int, data[2:]))

# Sort the moves in descending order
A.sort(reverse=True)

# Try to win the monster using the moves
for i in range(N):
    H -= A[i]
    if  H <= 0:
        print("Yes")
        exit()

print("No")