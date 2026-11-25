import sys

input = sys.stdin.read
data = input().split()
N, A = int(data[0]), list(map(int, data[1:]))

# Sort the monsters by their health in descending order
A.sort(reverse=True)

# The minimum possible final health of the last monster alive
# is the smallest health among the monsters
print(A[-1])
