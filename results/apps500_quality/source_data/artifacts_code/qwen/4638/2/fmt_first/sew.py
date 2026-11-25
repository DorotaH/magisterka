import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
c = int(data[1])

a = list(map(int, data[2 : 2 + n - 1]))
b = list(map(int, data[2 + n - 1 : 2 + 2 * (n - 1)]))

# Initialize the minimum time to reach each floor
t = [0] * n

# Calculate the minimum time to reach each floor
for i in range(1, n):
    t[i] = min(t[i - 1] + a[i - 1], t[i - 1] + c + b[i - 1])

# Print the results
print(" ".join(map(str, t)))