MOD = 1000000007

def count_complexity(x):
    n=len(x)
    count_0 = 0
    count_1 = 0
    for bit in x:
        if not bit == '0':
            count_1 += 1
        else:
            count_0 += 1
    complexity=(count_0 * count_1)%MOD
    return complexity

# Read input
x = input().strip()

# Calculate and print the complexity
print(count_complexity(x))