import math


def is_on_crust(radius, crust_width, sausage_center, sausage_radius):
    distance_from_center = math.sqrt(sausage_center[0]**2 + sausage_center[1]**2)
    main_part_radius = radius - crust_width
    if main_part_radius <= distance_from_center <= radius:
        return sausage_radius + crust_width >= distance_from_center
    return False


def main():
    import sys
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
        x = int(data[index])
        y = int(data[1 + index])
        r_s = int(data[2 + index])
        index += 3

        if is_on_crust(r, d, (x, y), r_s):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
