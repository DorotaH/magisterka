
L = float(input())

max_volume = 0
for a in range(1, int(L) + 1):
    for b in range(a, int(L) + 1):
        for c in range(b, int(L) + 1):
            if a + b + c == L:
                volume = a * b * c
                max_volume = max(max_volume, volume)

print(round(max_volume, 7))
