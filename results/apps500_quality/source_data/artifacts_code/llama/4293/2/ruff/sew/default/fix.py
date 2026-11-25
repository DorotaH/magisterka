P, Q, R = map(int, input().split())

min_sum = min(P + Q, P + R, Q + R)
print(min_sum)