import sys


def can_see_white_sheet():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    x5, y5, x6, y6 = map(int, sys.stdin.readline().split())

    # Check if white sheet is fully covered by black sheets
    if x3 <= x1 and x1 <= x4 and y3 <= y1 and y1 <= y4 and x2 <= x6 and y2 <= y6:
        return "NO"

    # Check if white sheet is partially visible
    if x1 < x3 and x4 < x2:
        if y1 > y3 and y4 > y1:
            return "YES"
        if y2 > y3 and y4 > y2:
            return "YES"

    if x1 < x5 and x6 < x2:
        if y1 > y5 and y6 > y1:
            return "YES"
        if y2 > y5 and y6 > y2:
            return "YES"

    # Check if there are any points outside the white sheet but inside the black sheets
    if x3 <= x1 and x2 <= x4 and (y3 <= y1 and y2 <= y4):
        return "YES"
    if x5 <= x1 and x2 <= x6 and (y5 <= y1 and y2 <= y6):
        return "YES"

    # Check if the corner points of white sheet are inside the black sheets
    if x3 <= x1 and x1 <= x4 and y3 <= y1 and y1 <= y4:
        return "NO"
    if x2 <= x5 and x6 <= x2 and y2 <= y5 and y6 <= y2:
        return "NO"

    return "YES"


print(can_see_white_sheet())
