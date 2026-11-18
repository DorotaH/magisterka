class Solver:
    def __init__(self):
        pass

    def solve(self):
        n, t, k, d = list(map(int, input().split()))
        n = (n + k - 1) // k
        if d < (n - 1) * t:
            print("YES")
        else:
            print("NO")


def __starting_point():
    s = Solver()
    s.solve()


__starting_point()
