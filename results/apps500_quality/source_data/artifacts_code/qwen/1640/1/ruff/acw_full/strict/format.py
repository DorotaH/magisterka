def calculate_d_sum(n, a):
    a.sort()
    count = [0] * n
    count[0] = 1
    for i in range(1, n):
        count[i] = count[i - 1] if a[i] == a[i - 1] else i + 1 - count[i - 1]
    return sum((n - i - count[i]) * (count[i] - 1) for i in range(n))


# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
print(calculate_d_sum(n, a))
