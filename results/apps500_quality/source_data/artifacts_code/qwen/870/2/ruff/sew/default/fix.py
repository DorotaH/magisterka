d, L, v1, v2 = map(int, input().split())

# The relative speed at which the distance between the presses decreases
relative_speed = v1 + v2

# The time Luke can stay alive
time_luke_can_stay_alive = (L - d) / relative_speed

print(time_luke_can_stay_alive)