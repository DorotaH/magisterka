import sys

input = sys.stdin.read
data = input().split()

S = data[0]

min_diff = float('inf')

for i in range(len(S) - 2):
    X = int(S[i:i+3])
    diff = abs(X - 753)
    min_diff = min(min_diff, diff)

print(min_diff)
