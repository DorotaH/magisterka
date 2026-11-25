import  sys

x1, x2, x3 = map(int, input().split())


def  calculate_distance(x):
    return abs(x-x1)+abs(x-x2)+abs(x-x3)


def  calculate_minimum_distance():
    distances = []
    for x in range(min(x1, x2, x3), max(x1, x2, x3) + 1):
        distances.append(calculate_distance(x))
    return min(distances)

print(calculate_minimum_distance())