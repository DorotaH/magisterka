def is_ladder(a, l, r):
    """Check if a subsegment of a is a ladder."""
    if l == r:
        return "Yes"
    increasing = decreasing = True
    for i in range(l, r - 1):
        if a[i] > a[i + 1]:
            increasing = False
        if a[i] < a[i + 1]:
            decreasing = False
        if not increasing and not decreasing:
            return "No"
    return "Yes"


def main():
    """Main function to solve the problem."""
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(m):
        l, r = map(int, input().split())
        print(is_ladder(a, l - 1, r))


if __name__ == "__main__":
    main()
