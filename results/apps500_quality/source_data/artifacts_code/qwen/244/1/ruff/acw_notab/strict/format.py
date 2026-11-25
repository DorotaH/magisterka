n, x = map(int, input().split())

# Determine the initial position of the ball
if n % 2 == 0:
    initial_position = x
elif x == 0:
    initial_position = 1
elif x == 1:
    initial_position = 2
else:
    initial_position = 0

print(initial_position)
