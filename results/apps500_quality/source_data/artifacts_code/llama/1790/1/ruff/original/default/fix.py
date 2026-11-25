from sys import stdin


def solve(stops):
    intersection = set(stops[0])
    for stop in stops[1:]:
        intersection &= set(stop)
    return sorted(list(intersection))

n = int(stdin.readline())
stops = [list(map(int, stdin.readline().split()))[1:] for _ in range(n)]
print(' '.join(map(str, solve(stops))))
