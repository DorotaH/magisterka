p, q, r = map(int, input().split())
min_sum = min(q + p, q + r, r + p, q + r)
print(min_sum)
