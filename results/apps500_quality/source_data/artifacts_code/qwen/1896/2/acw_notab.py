def count_hexagons(n):
    return 3 * n * (1 + n) + 1


n = int(input())
print(count_hexagons(n))
