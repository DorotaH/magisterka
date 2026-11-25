x1, x2, x3 = map(int, input().split())
sorted_x = sorted([x1, x2, x3])
median = sorted_x[1]
total_distance = abs(x1 - median) + abs(x2 - median) + abs(x3 - median)
print(total_distance)