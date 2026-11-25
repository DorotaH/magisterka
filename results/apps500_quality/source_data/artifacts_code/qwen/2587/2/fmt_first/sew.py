import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
results = []

for i in range(t):
    n = int(data[1 + 2 * i])
    if not n == 1:
        results.append("9" * (n - 1) + "8")
    else:
        results.append("8")

print("\n".join(results))