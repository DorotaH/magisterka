n, m = map(int, input().split())
teleports = [tuple(map(int, input().split())) for _ in range(n)]

# Sort teleports by their starting point
teleports.sort()

# Initialize the current position of Pig
current_position = 0

# Try to reach the friend's house using teleports
for start, limit in teleports:
    if start <= current_position <= limit:
        current_position = limit

# Check if Pig has reached the friend's house
if current_position == m:
    print("YES")
else:
    print("NO")
