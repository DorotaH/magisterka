n, m, k = map(int, input().split())
a, b = map(int, input().split())

a -= 1
b -= 1
distance = abs((b - a) % (n * m * k))
shortest_distance = min(distance, (n * m * k) - distance)

lift_time = 19
horizontal_time, downward_distance = (
    15 * n,
    shortest_distance - (shortest_distance // n) * m,
)
downward_time, upward_distance = (
    5 * downward_distance,
    shortest_distance - downward_distance,
)
upward_time = 5 * (upward_distance - (upward_distance // n) * m)

print(
    min(lift_time + horizontal_time, lift_time + downward_time, lift_time + upward_time)
)
