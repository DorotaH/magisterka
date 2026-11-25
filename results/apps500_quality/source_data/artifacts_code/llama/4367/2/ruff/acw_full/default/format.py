n, r = map(int, input().split())
inner_rating = r + 100 * (10 - n) * (10 > n)
print(inner_rating)
