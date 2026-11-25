import sys
from math import sqrt


def is_on_crust(x, y, r, d):
    distance = sqrt(x**2 + y**2)
    if distance + r > r - d and distance - r < r - d:
        return True
    return False

def main():
    input = sys.stdin.read
    data = input().split()

    r = int(data[0])
    d = int(data[1])
    n = int(data[2])

    sausage_positions = [(int(data[3 + 3*i]), int(data[4 + 3*i]), int(data[5 + 3*i])) for i in range(n)]

    count = 0
    for x, y, r in sausage_positions:
        if is_on_crust(x, y, r, d):
            count += 1

    print(count)

if __name__ == "__main__":
    main()
