import sys


def count_hexagons(n):
    # The formula to calculate the number of hexagons within a distance n from a given hexagon
    return 3 * n * (n + 1) + 1

if __name__ == "__main__":
    n = int(sys.stdin.read().strip())
    print(count_hexagons(n))
