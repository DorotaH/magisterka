def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2


def intersect2(x1, y1, x2, y2, x3, y3, x4, y4):
    return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2


def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if white sheet is not intersected by the first black sheet
    if not intersect(x1, y1, x2, y2, x3, y3, x4, y4):
        return "YES"

    # Check if white sheet is not intersected by the second black sheet
    if not intersect2(x1, y1, x2, y2, x5, y5, x6, y6):
        return "YES"

    # Check if white sheet is not fully covered by both black sheets
    if x1 < x5 or x2 > x6 or y1 < y3 or y2 > y4:
        return "YES"

    # Check if white sheet is intersected by both black sheets
    if intersect(x1, y1, x2, y2, x5, y5, x6, y6) and intersect2(
        x1, y1, x2, y2, x3, y3, x4, y4
    ):
        x_intersect = max(x3, min(x2, x6))
        y_intersect = max(y3, min(y2, y4))
        x1_intersect = min(x1, min(x4, x5))
        y1_intersect = min(y1, min(y4, y5))
        if x_intersect <= x1_intersect and y_intersect <= y1_intersect:
            return "YES"

    return "NO"


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

print(can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))
