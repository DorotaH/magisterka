import sys


def  solve():
    n, u = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
    last = dict()
    last_count, max_streak = {}, 0
    for i in range(n):
        last[u[i]] = i
        last_count[u[i]] = last_count.get(u[i], 0) + 1
        if len(last_count)>10:
            max_streak=max(max_streak, i-last[u[i-10]])
            last_count[u[i-10]-1]-=1
            if  0 == last_count[u[i - 10] - 1]:
                del  last_count[u[i - 10] - 1]
        for color in list(last_count):
            if  last_count[color] > 1:
                max_streak=max(max_streak, i-last[color])
                last_count[color]-=1
                if 0 == last_count[color]:
                    del  last_count[color]
    max_streak = max(max_streak, n)
    print(max_streak)

if __name__ == "__main__":
    solve()