# Read input from standard input
n, a = int(input()), list(map(int, input().split()))

# Sort the list to easily find the third largest element
a.sort()

# Output the third largest element
print(a[n - 3])