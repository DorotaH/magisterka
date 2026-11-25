n, r = map(int, input().split())
inner_rating = r + (100 * (10 - n) * (n < 10))
print(inner_rating)