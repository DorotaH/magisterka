import sys
input = sys.stdin.read
data = input().split()

N, A = int(data[0]), int(data[1])
B = int(data[2])

fee_plan_1, fee_plan_2 = A * N, B

min_fee = min(fee_plan_1, fee_plan_2)
print(min_fee)