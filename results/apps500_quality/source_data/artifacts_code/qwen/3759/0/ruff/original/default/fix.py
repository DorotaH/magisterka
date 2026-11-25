import sys


def min_points_to_block(n):
    return n * n

if __name__ == "__main__":
    n = int(sys.stdin.read().strip())
    print(min_points_to_block(n))
