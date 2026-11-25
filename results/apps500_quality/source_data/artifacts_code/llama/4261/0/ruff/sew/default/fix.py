A, B, C = map(int, input().split())
water_transferred = B
C -= water_transferred
C = max(C, 0)
print(C)