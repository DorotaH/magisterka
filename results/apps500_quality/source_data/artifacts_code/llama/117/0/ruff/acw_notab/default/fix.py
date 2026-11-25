import sys


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def intersect(self, other):
        if self.b == other.b:
            return None
        return (self.b - other.b) / (self.a - other.a), ((self.b - other.b) * self.a - other.a * (self.b - other.b)) / (self.a - other.a)


def calc_area(north_lines, east_lines):
    INF = 2 * 10 ** 18
    if len(north_lines) == 0 or len(east_lines) == 0:
        return INF
    if len(north_lines) == 1 and len(east_lines) == 1:
        return INF

    north_lines.sort(key=lambda line: line.b)
    east_lines.sort(key=lambda line: line.b)

    x_intersect = None
    for i in range(1, len(north_lines)):
        intersect = north_lines[i - 1].intersect(north_lines[i])
        if intersect is not None and (x_intersect is None or x_intersect[0] > intersect[0]):
            x_intersect = intersect

    if x_intersect is None:
        return INF

    y_intersect = None
    for i in range(1, len(east_lines)):
        intersect = east_lines[i - 1].intersect(east_lines[i])
        if intersect is not None and (y_intersect is None or y_intersect[0] < intersect[0]):
            y_intersect = intersect

    if y_intersect is None:
        return INF

    left_x = y_intersect[0] - north_lines[0].b
    right_x = y_intersect[0] - north_lines[-1].b
    top_y = max(north_lines[-1].b, y_intersect[1])
    bottom_y = min(north_lines[0].b, y_intersect[1])

    if top_y - bottom_y > right_x - left_x:
        return INF

    return (top_y - bottom_y) * (right_x - left_x)


def main():
    input_lines = sys.stdin.readlines()
    N, M = map(int, input_lines[0].split())
    north_lines = []
    east_lines = []
    for i in range(1, N + 1):
        line = list(map(int, input_lines[i].split()))
        north_lines.append(Line(line[0], line[2]))
    for i in range(N + 1, N + M + 1):
        line = list(map(int, input_lines[i].split()))
        east_lines.append(Line(line[1], line[2]))
    print(calc_area(north_lines, east_lines))


if __name__ == "__main__":
    main()
