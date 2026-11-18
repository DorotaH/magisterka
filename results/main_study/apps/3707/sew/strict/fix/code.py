
class  Solver:
    def  __init__(self):
        ...
    def  solve(self):
        n, t, k, d = list(map(int, input().split()))
        n = (k + n - 1) // k
        if not d < (n-1) * t:
            print('NO')
        else:
            print('YES')

def  __starting_point():
    s = Solver()
    s.solve()

__starting_point()
