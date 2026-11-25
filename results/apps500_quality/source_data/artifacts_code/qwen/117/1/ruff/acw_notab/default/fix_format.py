from fractions import Fraction


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    det = dx1 * dy2 - dy1 * dx2
    if det == 0:
        return None
    t = Fraction(dy2 * (x3 - x1) - (y3 - y1) * dx2, det)
    s = Fraction(dy1 * (x3 - x1) - dx1 * (y3 - y1), det)
    return (x1 + t * dx1, y1 + t * dy1) if 0 <= t <= 1 and 0 <= s <= 1 else None


def convex_hull(points):
    points.sort(key=lambda p: (p[0], p[1]))
    lower = []
    for p in points:
        while 2 <= len(lower) and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while 2 <= len(upper) and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def cross(p1, p2, p3):
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) - (p3[0] - p1[0]) * (p2[1] - p1[1])


def area(points):
    if 2 >= len(points):
        return 0
    return (
        sum(
            cross(
                points[i], points[(i + 1) % len(points)], points[(i + 2) % len(points)]
            )
            for i in range(len(points))
        )
        // 2
    )


def solve():
    N, M = map(int, input().split())
    ns_lines = []
    ew_lines = []
    for _ in range(N):
        A, B, C = map(int, input().split())
        ns_lines.append(((A, C), (B, C)))
    for _ in range(M):
        D, E, F = map(int, input().split())
        ew_lines.append(((D, E), (D, F)))

    points = [(0, 0)]
    for (A, C), (B, C) in ns_lines:
        points.extend(((A, C), (B, C)))
    for (D, E), (D, F) in ew_lines:
        points.extend(((D, E), (D, F)))
    points = list(set(points))
    if len(points) == 1:
        print("INF")
        return

    convex = convex_hull(points)
    if len(convex) <= 2:
        print("INF")
        return

    area_value = area(convex)
    print(area_value)


if __name__ == "__main__":
    solve()
