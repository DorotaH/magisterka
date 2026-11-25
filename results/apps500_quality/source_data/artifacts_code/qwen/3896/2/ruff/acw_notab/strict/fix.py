MOD = 1000000007


def calculate_complexity(x):
    n = len(x)
    count = sum((1 << (n - i - 1)) for i in range(n) if x[i] == '1')
    return (count * (count - 1) // 2) % MOD


# Read input
x = input().strip()

# Calculate and print the complexity
result = calculate_complexity(x)
print(result)
