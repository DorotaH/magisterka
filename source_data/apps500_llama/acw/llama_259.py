# Read the input from standard input
a = int(input())
b = int(input())
h = int(input())

# Check if h is even
if h % 2 != 0:
	print("Error: Height must be even.")
else:
	# Calculate the area of the trapezoid
	area = 0.5 * (a + b) * h
	print(area)
