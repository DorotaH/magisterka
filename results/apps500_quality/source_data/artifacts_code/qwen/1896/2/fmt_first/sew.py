def  count_hexagons(n):
    return  1 + 3 * n * (n + 1)


n = int(input())
print(count_hexagons(n))
