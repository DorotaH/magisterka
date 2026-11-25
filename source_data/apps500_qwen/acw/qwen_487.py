import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Sort the monsters by their health in descending order
A.sort(reverse=True)

# The minimum possible final health of the last monster alive
# is the smallest health among the monsters
print(A[-1])
