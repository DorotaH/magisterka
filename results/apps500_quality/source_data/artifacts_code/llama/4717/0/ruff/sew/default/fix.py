# Read input from standard input
x, a, b = map(int, input().split())

# Determine which store is closer to Snuke's residence
if not abs(x - a) < abs(x - b):
    print('B')
else:
    print('A')