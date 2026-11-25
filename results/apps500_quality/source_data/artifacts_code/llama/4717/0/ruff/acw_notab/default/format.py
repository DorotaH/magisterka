# Read input from standard input
x, a, b = map(int, input().split())

# Determine which store is closer to Snuke's residence
if abs(x - a) < abs(x - b):
    print("A")
else:
    print("B")
