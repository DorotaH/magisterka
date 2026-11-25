P, Q, R = map(int, input().split())

min_sum = min(P + Q, R + P, R + Q)
print(min_sum)
