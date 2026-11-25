import sys
from math import sqrt


def is_on_crust(x, y, r, d):
    distance = sqrt(x**2 + y**2)
    return distance + r > r - d and distance - r < r - d


def main():
    input = sys.stdin.read
    data = input().split()

    r = int(data[0])
    d = int(data[1])
    n = int(data[2])

    sausage_positions = [
        (int(data[3 + i * 3]), int(data[4 + i * 3]), int(data[5 + i * 3]))
        for i in range(n)
    ]

    count = sum(bool(is_on_crust(x, y, r, d))
            for x, y, r in sausage_positions)
    print(count)


if __name__ == "__main__":
    main()
