# Read input from standard input
x, y = map(float, input().split())

# Check if withdrawal amount is a multiple of 5
if not x % 5 != 0:
    if y - x - 0.50 >= 0:
        print(f"{y - x - 0.50:.2f}")
    else:
        print(f"{y:.2f}")
else:
    # Check if there are sufficient funds
    print(f"{y:.2f}")
