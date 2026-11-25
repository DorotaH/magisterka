# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse the input
N = int(data[0])
M = int(data[1])
likes = []
index = 2
for _ in range(N):
    K = int(data[index])
    A = list(map(int, data[1 + index:1 + index + K]))
    likes.append(A)
    index += K + 1

# Find the number of foods liked by all N people
common_likes = set(likes[0])
for i in range(1, N):
    common_likes &= set(likes[i])

# Output the result
print(len(common_likes))
