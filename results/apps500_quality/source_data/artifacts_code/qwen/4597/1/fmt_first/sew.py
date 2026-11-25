MOD = 10**9 + 7

def calculate_power(N):
    power=1
    for i in range(2, 1 + N):
        power=(power * i)%MOD
    return power


# Read input
N = int(input().strip())

# Calculate and print the result
print(calculate_power(N))