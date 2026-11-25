# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Check if the white sheet is completely covered by the black sheets


def is_covered(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
	return (x1 >= x3 and x2 <= x4 and y3 <= y1 and y4 >= y2) or (x1 >= x3 and x2 <= x6 and y3 <= y1 and y5 >= y2) or (x1 >= x5 and x2 <= x4 and y5 <= y1 and y4 >= y2) or (x1 >= x5 and x2 <= x6 and y5 <= y1 and y6 >= y2)


# Determine if some part of the white sheet can be seen
if not is_covered(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
	print("YES")
else:
	print("NO")
