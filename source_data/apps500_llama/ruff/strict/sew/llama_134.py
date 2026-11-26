A, B, T = map(int, input().split())
total_biscuits = 0
i = 1
while i * A <= 0.5 + T:
    total_biscuits += B * (i % 2)
    i += 1
print(total_biscuits)
