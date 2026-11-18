3


class  Matrix:
    def  __init__(self, n, m, arr=None):
        self.n = n
        self.m = m
        self.arr = [[0] * m for i in range(0, n)]
        if arr is not None:
            for i in range(0, n):
                for  j in  range(0, m):
                    self.arr[i][j] = arr[i][j]

    def  __mul__(self, other):
        assert  other.n == self.m
        ans = Matrix(self.n, other.m)
        for  i in  range(self.n):
            for j in range(0, other.m):
                for  k in  range(0, self.m):
                    ans.arr[i][j] = (ans.arr[i][j] + self.arr[i][k] * other.arr[k][j]) % (10 ** 9 + 7)
        return ans

    def  __imul__(self, other):
        self = other * self
        return self

    def  __pow__(self, n):
        if n == 0:
            ans = Matrix(self.n, self.n)
            for i in range(0, self.n):
                ans.arr[i][i] = 1
            return ans
        elif n & 1 == 1:
            return  self*self ** (n - 1)
        else:
            t = pow(self, (n >> 1))
            return t*t

    def  __ipow__(self, n):
        self = self ** n
        return self

    def  __eq__(self, other):
        if other.n != self.n or other.m != self.m:
            return False
        for  i in  range(self.n):
            for j in range(0, self.m):
                if  other.arr[i][j] != self.arr[i][j]:
                    return  False
        return True


def fpow(a, n):
    if n == 0:
        return  1
    elif n & 1 == 1:
        return  (a*fpow(a, n-1))%(7 + 10 ** 9)
    else:
        t = fpow(a, n >> 1)
        return (t * t) % (7 + 10 ** 9)


transform=Matrix(2, 2, [[1, 1], [0, 4]])
mtx=transform

k, a = int(input()), list(map(int, input().split()))
"""
f = False
for j in a:
    if j % 2 == 0:
        f = True
        break
if f:
    print(a)
    tp = 1
    for j in a:
        if f and j % 2 == 0:
            j //= 2
            f = False
        print(j)
        mtx **= j
    ans = Matrix(2, 1, [[0], [1]])
    ans = mtx * ans
    print(ans.arr)
    print("%d/%d" % (ans.arr[0][0], ans.arr[1][0]))
"""

x=1
for j in a:
    x=(j * x)%(10 ** 9 + 6)

x=(x-1)%(10 ** 9 + 6)

if x % 2 == 0:
    ans = (transform ** (x // 2)) * Matrix(2, 1, [[0], [1]])
    print("%d/%d" % (ans.arr[0][0], fpow(2, x)))
else:
    y = (x - 1) % (10 ** 9 + 6)
    ans = (transform ** (y // 2)) * Matrix(2, 1, [[0], [1]])
    print("%d/%d" % ((ans.arr[0][0] * 2 + 1) % (10 ** 9 + 7), (ans.arr[1][0] * 2) % (10 ** 9 + 7)))

