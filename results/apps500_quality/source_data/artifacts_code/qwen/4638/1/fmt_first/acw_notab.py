import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
c = int(data[1])

a = list(map(int, data[2 : 1 + n]))
b = list(map(int, data[1 + n : 2 * n]))

# Initialize the minimum time to reach each floor
t = [0] * n
t[0] = 0  # Starting floor is already at floor 1

# Calculate the minimum time to reach each floor using the stairs and elevator
for i in range(1, n):
    t[i] = min(a[i - 1] + t[i - 1], t[i - 1] + c + b[i - 1])

# Print the results
print(" ".join(map(str, t)))
