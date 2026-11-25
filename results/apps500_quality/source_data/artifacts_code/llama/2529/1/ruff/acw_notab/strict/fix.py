
# Read input from standard input
x, y = map(float, input().split())

# Check if withdrawal amount is a multiple of 5
if x % 5 == 0 and y - x - 0.50 >= 0:
    print(f"{y - x - 0.50:.2f}")
else:
    print(f"{y:.2f}")
