import math
import sys


def is_on_crust(center_x, center_y, radius, radius_crust):
    distance_from_center = math.sqrt(center_y**2 + center_x**2)
    return radius - radius_crust <= distance_from_center <= radius


def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    r = int(data[index])
    d = int(data[1 + index])
    index += 2

    n = int(data[index])
    index += 1

    count = 0
    for _ in range(n):
        center_x = int(data[index])
        center_y = int(data[1 + index])
        radius = int(data[2 + index])
        index += 3

        if is_on_crust(center_x, center_y, r, d):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
