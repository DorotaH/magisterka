# Read input
n, m = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

# Sort the lantern brightnesses
a.sort()
b.sort()

# Tommy will hide the lantern with the smallest brightness
# Banban will choose the smallest lantern from Tommy and the largest from himself
min_brightness = min(b[0] * a[0], b[-1] * a[0])

# Output the result
print(min_brightness)
