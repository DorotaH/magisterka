n = int(input())
ratings = list(map(int, input().split()))

min_colors = len(set(r for r in ratings if r < 3200))
max_colors = len(set(f(r) for r in ratings))


def f(r):
    if r < 400:
        return "gray"
    elif r < 800:
        return "brown"
    elif r < 1200:
        return "green"
    elif r < 1600:
        return "cyan"
    elif r < 2000:
        return "blue"
    elif r < 2400:
        return "yellow"
    elif r < 2800:
        return "orange"
    elif r < 3200:
        return "red"
    else:
        return "gray"


print(min_colors, max_colors)
