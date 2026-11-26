import math


def max_rectangle_area(W, H, x, y):
    # Calculate the total area of the rectangle
    total_area = H * W

    # Calculate the maximum area of one part by cutting the rectangle in half
    max_area = (H * W) / 2

    # The maximum area is achieved when the cut line passes through the point (x, y)
    # If the cut line passes through the point (x, y), the area of one part is
    #   (x * H) or (W * y - x * y)
    # The other area is (W * H - x * H) or (W * y - x * y)
    # In either case, one area is larger than the other, so the area of the other part is
    #   (W * H - x * H) or (W * y - x * y)
    max_area = min(max_area, (W * H) - (x * H), (W * y) - (x * y))

    # If the cut line passes through the point (x, y), the other part is a trapezoid
    # The area of a trapezoid is ((base1 + base2) / 2) * height
    # In this case, the bases are x and W - x, the height is y
    # So the area of the trapezoid is ((x + W - x) / 2) * y = (W / 2) * y
    # The area of the trapezoid is less than the area of the rectangle, so the area of the trapezoid is
    #   (W / 2) * y
    max_area = min(max_area, (W / 2) * y)

    # If the cut line passes through the point (x, 0), the area of one part is x * H
    # The other part is a rectangle with area (W * H - x * H)
    # If x * H is larger than or equal to (W * H - x * H), then the area of the part with the trapezoid is
    #   (W * H - x * H)
    # If x * H is less than (W * H - x * H), then the area of the part with the trapezoid is
    #   x * H
    max_area = min(max_area, (W * H) - (x * H), H * x)

    # If the cut line passes through the point (0, y), the area of one part is y * W
    # The other part is a rectangle with area (H * y - y * W)
    # If y * W is larger than or equal to (H * y - y * W), then the area of the part with the trapezoid is
    #   H * y - y * W
    # If y * W is less than (H * y - y * W), then the area of the part with the trapezoid is
    #   y * W
    max_area = min(max_area, (H * y) - (y * W), W * y)

    # If the cut line passes through the point (0, 0), the area of one part is 0
    # The other part is the rectangle with area W * H
    # So the area of the part with the trapezoid is W * H
    max_area = min(max_area, H * W)

    # Check if there are multiple ways to achieve the maximum area
    # If there are multiple ways, then the maximum area is achieved when the cut line passes through the point (x, y)
    # and when the cut line passes through the point (0, y)
    # The area of one part when the cut line passes through the point (x, y) is (W * y - x * y)
    # The area of one part when the cut line passes through the point (0, y) is (H * x)
    # If (W * y - x * y) is equal to (H * x), then there are multiple ways to achieve the maximum area
    multiple_ways = ((W * y) - (x * y)) == (H * x)

    return f"{max_area:.10f} {'1' if multiple_ways else '0'}"


W, H, x, y = map(int, input().split())
print(max_rectangle_area(W, H, x, y))
