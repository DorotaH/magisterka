A, B, C = map(int, input().split())
water_transferred = B
C -= water_transferred
if  C<0:
    C=0
print(C)
