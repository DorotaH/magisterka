def can_choose_balls():
    n, balls = int(input()), sorted(map(int, input().split()))

    for  i in  range(n - 2):
        if balls[1 + i] - balls[i] > 2 or balls[2 + i] - balls[1 + i] > 2 or balls[1 + i] - balls[i] < 2:
            return "NO"

    return  "YES"

print(can_choose_balls())
