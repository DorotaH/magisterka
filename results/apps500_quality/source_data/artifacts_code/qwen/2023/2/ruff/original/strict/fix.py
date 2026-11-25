from sys import stdin, stdout

# Read input
input = stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])

a = list(map(int, data[2:2+n]))
b = list(map(int, data[2+n:2+2*n]))

# Initialize output list
output = []

# Process queries
index = 2 + 2 * n
for i in range(m):
    t = int(data[index])
    if t == 1:
        x = int(data[index + 1]) - 1
        y = int(data[index + 2]) - 1
        k = int(data[index + 3])
        for j in range(k):
            b[y + j] += a[x + j]
    elif t == 2:
        x = int(data[index + 1]) - 1
        output.append(b[x])
    index += 4

# Print output
for value in output:
    stdout.write(f"{value}\n")
