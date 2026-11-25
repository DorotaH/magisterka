
# Read input from standard input
N, A, B = map(int, input().split())

# Calculate the minimum fee
min_fee = min(A * N, B)

# Print the minimum fee
print(min_fee)
