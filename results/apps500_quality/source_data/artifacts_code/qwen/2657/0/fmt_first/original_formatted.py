import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))

# Sort the array to make it easier to find the maximum combination
a.sort()

# Initialize variables to store the maximum combination and the corresponding pair
max_comb = 0
result_pair = (0, 0)

# Iterate through the sorted array to find the maximum combination
for i in range(n - 1):
    for j in range(i + 1, n):
        comb = a[i] * (a[i] - 1) // 2 + a[j] * (a[j] - 1) // 2
        if comb > max_comb:
            max_comb = comb
            result_pair = (a[i], a[j])

# Print the result
print(result_pair[0], result_pair[1])
