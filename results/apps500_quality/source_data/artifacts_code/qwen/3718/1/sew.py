def can_choose_balls(n, balls):
    balls.sort()
    for i in range(0, n - 2):
        if balls[i + 2]-balls[i]<=2:
            return  "YES"
    return  "NO"

# Read input
import  sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
balls = list(map(int, data[1:]))

# Output result
print(can_choose_balls(n, balls))
