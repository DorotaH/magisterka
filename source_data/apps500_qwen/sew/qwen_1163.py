def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if the white sheet is completely covered by both black sheets
    if not (x1 >= x4 and x2 <= x3 and y1 >= y4 and y2 <= y3 and x1 >= x6 and x2 <= x5 and y1 >= y6 and y2 <= y5):
        return "YES"
    else:
        return "NO"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Determine if some part of the white sheet can be seen
result = can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)
print(result)
