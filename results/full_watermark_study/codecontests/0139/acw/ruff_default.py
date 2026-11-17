import sys

input = lambda: sys.stdin.readline().rstrip()

write = lambda x: sys.stdout.write("\n" + x)
debug = lambda x: sys.stderr.write("\n" + x)
writef = lambda x: print(f"{x:.12f}")
# sys.setrecursionlimit(3*10**5+10)
### セグメント木(はやい)


class SG:
    def __init__(self, n, v=None):
        self._n = n
        self.geta = 0
        x = 0
        while n > (1 << x):
            x += 1
        self._log = x
        self._size = 1 << self._log
        self._d = [ninf] * (self._size * 2)
        if v is not None:
            for i in range(self._n):
                self._d[i + self._size] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k):
        self._d[k] = op(self._d[2 * k], self._d[2 * k + 1])

    def update(self, p, x):
        assert 0 <= p < self._n
        #         x -= self.geta
        p += self._size
        self._d[p] = x
        for i in range(1, 1 + self._log):
            #             self._update(p >> i)
            k = p >> i
            self._d[k] = op(self._d[2 * k], self._d[2 * k + 1])

    def get(self, p):
        assert 0 <= p < self._n
        return self._d[self._size + p]  # + self.geta

    def check(self):
        return [self.get(p) for p in range(self._n)]

    def query(self, left, right):
        # [l,r)の総和
        assert 0 <= left <= right <= self._n
        sml = ninf
        smr = ninf
        left += self._size
        right += self._size
        # 外側から計算していく(lは小さい側から, rは大きい側から)
        while left < right:
            if left & 1:
                sml = op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = op(self._d[right], smr)
            left >>= 1
            right >>= 1
        return op(sml, smr)  # + self.geta

    #     def update_all(self, v):
    #         # 全体加算
    #         self.geta += v

    def query_all(self):
        return self._d[1]  # + self.geta

    def max_right(self, left, f):
        """f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最大の r
        -> rはf(op(a[l:r+1]))がFalseになる最小のr
        """
        #         assert 0 <= left <= self._n
        #         assert f(ninf)
        if left == self._n:
            return self._n
        left += self._size
        sm = ninf
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(op(sm, self._d[left])):
                while self._size > left:
                    left *= 2
                    if f(op(sm, self._d[left])):
                        sm = op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = op(sm, self._d[left])
            left += 1
        return self._n

    def min_left(self, right, f):
        """f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最小の l"""
        #         assert 0 <= right <= self._n
        #         assert f(ninf)
        if right == 0:
            return 0
        right += self._size
        sm = ninf
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while 1 < right and right % 2:
                right >>= 1
            if not f(op(self._d[right], sm)):
                while self._size > right:
                    right = 2 * right + 1
                    if f(op(self._d[right], sm)):
                        sm = op(self._d[right], sm)
                        right -= 1
                return 1 + right - self._size
            sm = op(self._d[right], sm)
        return 0


op = min
ninf = 10**12

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ns = [[] for _ in range(1 + n)]
for i in range(1, 1 + n):
    #     if b[i-1]>0:
    ns[i + b[i - 1]].append(i)
ns[0].append(0)
sg = SG(1 + n, [0] + [i + 1 - a[i] for i in range(n)])
vs = [ninf] * (1 + n)
prv = [-1] * (1 + n)
prv[0] = 0
vs[0] = 0
from collections import deque

q = deque([0])
while q:
    u = q.popleft()
    val = vs[u]
    for v in ns[u]:
        c = v
        while c <= n:
            c = sg.max_right(c, lambda vv: vv > v)
            if c <= n:
                sg.update(c, ninf)
                vs[c] = val + 1
                prv[c] = v
                q.append(c)
if vs[n] >= ninf / 2:
    print(-1)
else:
    c = n
    ans = []
    while c != 0:
        c = prv[c]
        ans.append(c)
        c += b[c - 1]
    print(len(ans))
    write(" ".join(map(str, ans)))
