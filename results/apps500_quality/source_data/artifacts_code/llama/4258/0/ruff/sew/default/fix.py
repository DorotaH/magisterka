
A, B, T = map(int, input().split())
total_biscuits = t = 0

while t<=0.5 + T:
    total_biscuits+=B
    t+=A
    A += 1

print(int(total_biscuits))