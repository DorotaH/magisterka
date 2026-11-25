import sys


def hexagonal_distance(n):
    return 3 * n * (n + 1) // 2 + 1


if __name__ == "__main__":
    n = int(sys.stdin.read().strip())
    print(hexagonal_distance(n))
