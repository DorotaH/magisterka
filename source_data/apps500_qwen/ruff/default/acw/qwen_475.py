MOD = 1000000007


def count_complexity(x):
    n = len(x)
    count_0 = 0
    count_1 = 0
    for bit in x:
        if bit == "0":
            count_0 += 1
        else:
            count_1 += 1
    return (count_0 * count_1) % MOD


# Read input
x = input().strip()

# Calculate and print the complexity
print(count_complexity(x))
