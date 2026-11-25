n, a, x, b, y = map(int, input().split())

# Calculate the number of minutes it takes for Daniel to reach station x
daniel_minutes = (x - a) % n if a < x else (n - (a - x)) % n

# Calculate the number of minutes it takes for Vlad to reach station y
vlad_minutes = (y - b) % n if y > b else (n - (b - y)) % n

# Check if they will be at the same station at any time
if daniel_minutes == vlad_minutes:
    print("YES")
else:
    print("NO")
