n, a, x, b, y = map(int, input().split())

# Calculate the number of minutes it takes for Daniel to reach station x
if a < x:
    daniel_minutes = (x - a) % n
else:
    daniel_minutes = (n - (a - x)) % n

# Calculate the number of minutes it takes for Vlad to reach station y
if b < y:
    vlad_minutes = (y - b) % n
else:
    vlad_minutes = (n - (b - y)) % n

# Check if they will be at the same station at any time
if not daniel_minutes == vlad_minutes:
    print("NO")
else:
    print("YES")
