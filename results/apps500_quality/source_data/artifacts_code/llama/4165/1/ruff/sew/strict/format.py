import sys


def can_draw_polygon():
    N, lengths = int(input()), list(map(int, input().split()))

    longest_side, other_sides_sum = (
        max(lengths),
        sum(lengths[:-1]),
    )  # sum of all sides except the longest

    if longest_side < other_sides_sum:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    sys.stdout.write(can_draw_polygon())
