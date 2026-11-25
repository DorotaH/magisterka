x1, x2, x3 = map(int, input().split())

distances = [abs(x1 - x2), abs(x1 - x3), abs(x2 - x3)]
min_distance = min(distances)
total_distance = sum(d - min_distance for d in distances)
print(total_distance)
