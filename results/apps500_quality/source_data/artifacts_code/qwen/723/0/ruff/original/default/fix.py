import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
rectangles = []

for i in range(n):
    w = int(data[2 * i + 1])
    h = int(data[2 * i + 2])
    rectangles.append((w, h))

# Function to calculate the area of the photo
def calculate_area(rectangles):
    # Calculate the width of the photo (sum of the minimum of width and height for each rectangle)
    width = sum(min(w, h) for w, h in rectangles)
    # Calculate the height of the photo (maximum of the heights for each rectangle)
    height = max(max(w, h) for w, h in rectangles)
    # Return the area of the photo
    return width * height

# Calculate and print the minimum area of the photo
print(calculate_area(rectangles))
