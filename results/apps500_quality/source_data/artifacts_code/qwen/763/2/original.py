def min_electricity(n, a):
    total_electricity = 0
    for i in range(n):
        total_electricity += a[i] * (2 * sum(abs(j - i) for j in range(n)))
    return total_electricity

# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the minimum electricity units
print(min_electricity(n, a))
