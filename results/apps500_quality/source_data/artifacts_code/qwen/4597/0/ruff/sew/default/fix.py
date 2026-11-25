MOD = 10**9 + 7

def calculate_power(N):
    power=1
    for i in range(2, 1 + N):
        power=(power * i)%MOD
    return power

# Read input from standard input
N = int(input().strip())

# Calculate and print the power modulo 10^9 + 7
print(calculate_power(N))