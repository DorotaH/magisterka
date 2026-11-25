import sys

# Read input from standard input
N, A, B = map(int, sys.stdin.readline().split())

# Calculate the fee for each plan
fee_plan_1, fee_plan_2 = A * N, B

# Print the minimum fee
print(min(fee_plan_1, fee_plan_2))