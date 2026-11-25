d, L, v1, v2 = map(int, input().split())

# calculate the time it takes for the presses to meet
t = L / (v2 + v1)

# calculate the optimal position for Luke
x = (t * v1 / 2 + v2 * t / 2 + L / 2) - d / 2

# calculate the time it takes for the presses to meet Luke
t_meet = (x - 0) / v1

# calculate the time it takes for the presses to meet after Luke has moved away from the left press
t_meet = max(t_meet, (L - x) / v2)

# calculate the time it takes for the presses to meet before Luke has moved towards the right press
t_meet = min(t_meet, t)

# calculate the maximum time Luke can stay alive
max_time = t_meet

print(round(max_time, 12))
