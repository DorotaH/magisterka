import sys

def min_moves(n):
    if n == 1:
        return 0
    return (n * n - 1) * (n * n - 2) // 2

input = sys.stdin.read
data = input().split()

t = int(data[0])
results = []

for i in range(1, t + 1):
    n = int(data[i])
    results.append(str(min_moves(n)))

print('\n'.join(results))
