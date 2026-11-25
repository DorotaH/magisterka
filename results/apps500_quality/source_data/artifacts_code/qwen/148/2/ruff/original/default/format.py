n, a, x, b, y = map(int, input().split())

# Calculate the relative positions of Daniel and Vlad
relative_a = a % n
relative_x = x % n
relative_b = b % n
relative_y = y % n

# Check if they will meet at any station
# They will meet if the difference in their positions is the same as the difference in their destinations
if (relative_a - relative_b) % n == (relative_x - relative_y) % n:
    print("YES")
else:
    print("NO")
