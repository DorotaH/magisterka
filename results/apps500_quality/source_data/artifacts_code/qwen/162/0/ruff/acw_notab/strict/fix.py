# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

hours = next((k // a[i] for i in range(n) if k % a[i] == 0), 1)
# Print the result
print(hours)
