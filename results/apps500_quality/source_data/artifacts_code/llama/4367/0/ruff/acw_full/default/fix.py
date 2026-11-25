n, r = map(int, input().split())
inner_rating = r + 100 * max(0, 10 - n) * n
print(inner_rating)
