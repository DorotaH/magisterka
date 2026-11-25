n, a, x, b, y = map(int, input().split())

# Calculate the relative positions of Daniel and Vlad
relative_a, relative_x = a % n, x % n
relative_b, relative_y = b % n, y % n

# Check if they will meet at any station
# They will meet if the difference in their positions is the same as the difference in their destinations
if not (relative_a - relative_b) % n == (relative_x - relative_y) % n:
    print("NO")
else:
    print("YES")
