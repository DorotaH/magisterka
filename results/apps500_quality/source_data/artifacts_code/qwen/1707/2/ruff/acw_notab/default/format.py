n = int(input())
a = list(map(int, input().split()))

# Sort the array to facilitate finding valid pairs
a.sort()

# Initialize the count of valid pairs
count = 0

# Iterate through the array to find valid pairs
for i in range(n):
    for j in range(i + 1, n):
        x, y = a[i], a[j]
        if abs(x - y) <= abs(x) <= abs(y + x) and abs(x - y) <= abs(y) <= abs(y + x):
            count += 1

print(count)
