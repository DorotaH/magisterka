x1, x2, x3 = map(int, input().split())

distances = [abs(x1 - x2), abs(x1 - x3), abs(x2 - x3)]
min_distance = min(distances)
total_distance = 0

for d in distances:
    total_distance += d - min_distance

print(total_distance)
