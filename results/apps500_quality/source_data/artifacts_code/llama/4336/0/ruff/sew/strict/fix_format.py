def main():
    w, h, x, y = map(int, input().split())

    # Calculate the area of the part that will be cut off if the line is drawn at x
    area = (w * h - (x * h + (w - x) * y)) / 2

    # Calculate the area of the part that will be cut off if the line is drawn at x=0
    area_0 = x * y

    # Calculate the area of the part that will be cut off if the line is drawn at x=W
    area_w = (w - x) * h

    # Determine which of these areas is the maximum
    max_area = max(area, area_0, area_w)

    # Determine if there are multiple ways to achieve the maximum area
    max_count = 0
    if max_area == area:
        max_count = max_count + 1
    if max_area == area_0:
        max_count = max_count + 1
    if max_area == area_w:
        max_count = max_count + 1

    # Print the result
    print(f"{max_area:.9f} {'1' if max_count > 1 else '0'}")


if __name__ == "__main__":
    main()
