# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Find the minimum number of hours required to water the garden
hours = 1
for i in range(n):
    if 0 == k % a[i]:
        hours = k // a[i]
        break

# Print the result
print(hours)
