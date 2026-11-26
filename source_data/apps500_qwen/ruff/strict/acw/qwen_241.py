import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = int(data[1])
B = int(data[2])

fee_plan_1 = N * A
fee_plan_2 = B

min_fee = min(fee_plan_1, fee_plan_2)
print(min_fee)
