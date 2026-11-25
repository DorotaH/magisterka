import sys
from math import sqrt


def is_on_crust(x, y, r, d):
    distance = sqrt(pow(x, 2) + pow(y, 2))
    if distance + r > r - d and distance - r < r - d:
        return True
    return False


def main():
    input = sys.stdin.read
    data = input().split()

    r = int(data[0])
    d = int(data[1])
    n = int(data[2])

    sausage_positions = []
    for i in range(n):
        sausage_positions.append(
            (int(data[3 + 3 * i]), int(data[4 + 3 * i]), int(data[5 + 3 * i]))
        )

    count = 0
    for x, y, r in sausage_positions:
        if is_on_crust(x, y, r, d):
            count = count + 1

    print(count)


if __name__ == "__main__":
    main()
