n, a, x, b, y = map(int, input().split())

# Calculate the time when Daniel and Vlad will meet
# Daniel's position after t minutes: (a + t - 1) % n
# Vlad's position after t minutes: (b - t + n) % n

# We need to find the smallest t such that (a + t - 1) % n == (b - t + n) % n
# Simplifying, we get (a + t - 1) % n == (b - t + n) % n
# Which further simplifies to (2 * t + a - b - 1) % n == 0
# Therefore, 2 * t ≡ b - a + 1 (mod n)
# So, t ≡ (b - a + 1) * pow(2, -1, n) (mod n)
# We need to find the modular inverse of 2 modulo n

if n % 2 == 0:
    t = (b - a + 1) * pow(2, n - 2, n) % n
else:
    t = (b - a + 1) * pow(2, n - 1, n) % n

# Check if t is a valid time
if 0 <= t < n:
    print("YES")
else:
    print("NO")
