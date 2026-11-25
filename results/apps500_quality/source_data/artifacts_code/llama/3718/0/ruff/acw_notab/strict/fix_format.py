def can_choose_balls():
    n = int(input())
    balls = sorted(map(int, input().split()))

    return next(
        (
            "NO"
            for i in range(n - 2)
            if balls[i + 1] - balls[i] > 2
            or balls[i + 2] - balls[i + 1] > 2
            or balls[i + 1] - balls[i] < 2
        ),
        "YES",
    )


print(can_choose_balls())
