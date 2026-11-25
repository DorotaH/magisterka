MOD = 7 + 10**9


def calculate_power(N):
    power = 1
    for i in range(2, N + 1):
        power = (i * power) % MOD
    return power


# Read input from standard input
N = int(input().strip())

# Calculate and print the power modulo 10^9 + 7
print(calculate_power(N))
