import sys


def read_input():
    return map(int, sys.stdin.readline().strip().split())


def main():
    t = next(read_input())
    for _ in range(t):
        n, k = read_input()
        l1, r1 = read_input()
        l2, r2 = read_input()

        l = min(l1, l2)
        r = max(r1, r2)
        intersection = min(l1, l2)
        total_intersection = n * intersection

        if k <= total_intersection:
            print(0)
            continue

        steps = (k - total_intersection + (2 * r) - (2 * l) - 1) // ((2 * r) - (2 * l))
        steps = steps + 1
        print(steps)


if __name__ == "__main__":
    main()
