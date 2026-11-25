def count_hexagons(n):
    return 3 * n * (n + 1) + 1

n = int(input())
print(count_hexagons(n))
