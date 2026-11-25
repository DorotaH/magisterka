import sys

input = sys.stdin.read
data = input().split()

x = int(data[0])

# The minimum number of steps required to reach x is the ceiling of x divided by 5
# because the elephant can move up to 5 positions in one step.
min_steps = (x + 4) // 5  # Equivalent to math.ceil(x / 5)

print(min_steps)
