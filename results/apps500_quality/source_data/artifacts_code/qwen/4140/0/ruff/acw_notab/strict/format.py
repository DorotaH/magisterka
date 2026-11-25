import sys

input = sys.stdin.read
data = input().split()

S = data[0]

repaints = sum(bool(S[i] == S[i - 1]) for i in range(1, len(S)))
# Output the minimum number of repaints
print(repaints)
