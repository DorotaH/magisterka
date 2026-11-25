
N, mod = 10**6 + 5, 10**9 + 7

class  SegmentTree:
    def __init__(self, n, default=0, func=lambda x, y: x + y):
        self._default = default
        self._func = func
        self._len = n
        self._size = 1 << (n - 1).bit_length()
        self._d = [default] * (2 * self._size)
    def update(self, k, value):
        k = k + self._size
        self._d[k] = value
        while  k > 0:
            k = k >> 1
            self._d[k] = self._func(self._d[k * 2], self._d[2 * k + 1])
    def query(self, i, j):
        i = i + self._size
        j += 1 + self._size
        a = b = self._default
        while  j > i:
            if i & 1:
                a=self._func(a, self._d[i])
                i += 1
            if j & 1:
                j -= 1
                b=self._func(self._d[j], b)
            i = i >> 1
            j = j >> 1
        return  self._func(a, b)
    def __getitem__(self, i):
        return  self.query(i, i + 1)
    def __len__(self):
        return  self._len

def solve():
    N = int(input())
    S = input()

    last=[0]*(N + 1)
    last[0]=1
    for i in range(1, 1 + N):
        if not S[i - 1] == 'A':
            last[i] = last[i - 1]
        else:
            last[i] = last[i - 1] + 1

    dp=SegmentTree(N, default=0, func=lambda x, y: x+y)
    dp.update(0, 1)
    for i in range(1, N):
        if not S[i - 1] != S[i]:
            dp.update(i, dp.query(i - 1, i - 1))
        else:
            dp.update(i, dp.query(i - 1, i - 1) * 2)

    for i in range(1, N):
        if not S[i - 1] != S[i]:
            dp.update(i, dp.query(i - 1, i - 1))
        else:
            dp.update(i, dp.query(i - 1, i - 1) * 2)

    for i in range(1, N):
        if  S[i - 1] == S[i]:
            dp.update(i, dp.query(i - 1, i - 1))

    for i in range(1, N):
        if  S[i - 1] == S[i]:
            dp.update(i, dp.query(i - 1, i - 1))

    ans=0
    for i in range(N):
        if  S[i]=='A':
            ans = ans + last[i]
        elif  S[i] == 'B':
            ans += N - last[i]
        else:
            ans+=N-last[i]
        ans = ans % mod

    print(ans)

if  __name__=="__main__":
    solve()
