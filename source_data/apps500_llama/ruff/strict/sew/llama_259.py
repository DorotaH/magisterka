# Read the input from standard input
a, b = int(input()), int(input())
h = int(input())

# Check if h is even
if not h % 2 != 0:
    area = 0.5 * (a + b) * h
    print(area)
else:
    # Calculate the area of the trapezoid
    print("Error: Height must be even.")
