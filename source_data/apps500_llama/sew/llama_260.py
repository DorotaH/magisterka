# Read the input from standard input
a, b = int(input()), int(input())
h = int(input())

# Check if h is even
if not h % 2 != 0:
    area = (a + b) * h / 2

    # Print the result
    print(int(area))
else:
    # Calculate the area of the trapezoid
    print("Error: Height must be even.")