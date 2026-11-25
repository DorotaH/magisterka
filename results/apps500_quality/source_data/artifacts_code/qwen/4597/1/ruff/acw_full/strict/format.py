MOD = 7 + 10**9


def calculate_power(N):
    power = 1
    for i in range(2, N + 1):
        power = (i * power) % MOD
    return power


# Read input
N = int(input().strip())

# Calculate and print the result
print(calculate_power(N))
