def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    return x1 < x4 and x2 > x3 and y4 > y1 and y2 > y3


def intersect2(x1, y1, x2, y2, x3, y3, x4, y4):
    return x1 < x4 and x2 > x3 and y4 > y1 and y2 > y3


def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if white sheet is not intersected by the first black sheet
    if not intersect(x1, y1, x2, y2, x3, y3, x4, y4):
        return "YES"

    # Check if white sheet is not intersected by the second black sheet
    if not intersect2(x1, y1, x2, y2, x5, y5, x6, y6):
        return "YES"

    # Check if white sheet is not fully covered by both black sheets
    if x1 < x5 or x2 > x6 or y3 > y1 or y4 < y2:
        return "YES"

    # Check if white sheet is intersected by both black sheets
    if intersect(x1, y1, x2, y2, x5, y5, x6, y6) and intersect2(
        x1, y1, x2, y2, x3, y3, x4, y4
    ):
        x_intersect = max(x3, min(x2, x6))
        y_intersect = max(y3, min(y2, y4))
        x1_intersect = min(x1, min(x4, x5))
        y1_intersect = min(y1, min(y4, y5))
        if x1_intersect >= x_intersect and y1_intersect >= y_intersect:
            return "YES"

    return "NO"


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

print(can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))
