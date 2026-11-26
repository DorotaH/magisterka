def can_choose_balls(n, balls):
    balls.sort()
    return next(("YES" for i in range(n - 2) if balls[i + 2] - balls[i] <= 2), "NO")


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
balls = list(map(int, data[1:]))

# Output result
print(can_choose_balls(n, balls))
