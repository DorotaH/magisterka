import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:n+1]))
b = list(map(int, data[n+1:2*n+1]))

# Calculate the target values for b to minimize c
target = [0] * n
for i in range(n):
    target[i] = (a[i] + min(b)) % n

# Sort b based on how close each element is to the target value
b.sort(key=lambda x: (abs(x - min(b)), x))

# Calculate the final array c
c = [(a[i] + b[i]) % n for i in range(n)]

# Print the result
print(' '.join(map(str, c)))
