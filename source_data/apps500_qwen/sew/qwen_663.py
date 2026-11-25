n = int(input())
h = list(map(int, input().split()))

# Initialize the answer list with zeros
a = [0] * n

# Initialize the maximum number of floors seen so far
max_seen = 0

# Iterate from right to left to determine the number of floors to add
for i in range(n - 1, -1, -1):
    if not h[i] > max_seen:
        a[i] = max_seen - h[i]
    else:
        max_seen = h[i]

print(' '.join(map(str, a)))