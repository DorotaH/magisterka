
r, c, n, k = map(int, input().split())

violins = []
for _ in range(n):
    x, y = map(int, input().split())
    violins.append((x, y))

count = 0
for top in range(1, r + 1):
    for left in range(1, c + 1):
        viola_count = 0
        for x, y in violins:
            if top <= x <= r and left <= y <= c:
                viola_count += 1
        if viola_count >= k:
            count += 1

print(count)
