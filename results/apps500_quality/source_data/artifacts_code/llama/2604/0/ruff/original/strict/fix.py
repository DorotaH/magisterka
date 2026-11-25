import math


def count_sausages_on_crust():
    r, d = map(int, input().split())
    n = int(input())
    count = 0

    for _ in range(n):
        x, y, radius = map(int, input().split())
        distance_from_center = math.sqrt(x**2 + y**2)
        if distance_from_center - radius > r - d:
            count += 1

    return count

print(count_sausages_on_crust())
