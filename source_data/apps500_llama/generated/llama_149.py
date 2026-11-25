p, q, r = map(int, input().split())
min_sum = min(p + q, r + q, p + r, q + r)
print(min_sum)
