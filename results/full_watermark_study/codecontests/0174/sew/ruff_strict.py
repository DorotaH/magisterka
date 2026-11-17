import os
import sys
from io import BytesIO, IOBase

M = 1000000007
# sys.setrecursionlimit(2*(10**5))
from collections import *
from functools import *
from itertools import *

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while 1:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if not sys.version_info[0] < 3:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
else:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


def inp():
    return sys.stdin.readline().rstrip("\r\n")  # for fast input


def out(var):
    sys.stdout.write(str(var))  # for fast output, always take string


def lis():
    return list(map(int, inp().split()))


def stringlis():
    return list(map(str, inp().split()))


def sep():
    return map(int, inp().split())


def strsep():
    return map(str, inp().split())


def fsep():
    return map(float, inp().split())


def inpu():
    return int(inp())


def build(a, b, st, arr, node):
    if a == b:
        st[node] = arr[a]
        return arr[a]
    mid = (a + b) // 2
    p, q = (
        build(a, mid, st, arr, 2 * node + 1),
        build(mid + 1, b, st, arr, 2 * node + 2),
    )
    st[node] = p + q
    return st[node]


def update(st, a, b, x, val, node):
    if x < a or b < x:
        return None
    st[node] = st[node] + val
    if a != b:
        mid = (a + b) // 2
        update(st, a, mid, x, val, 2 * node + 1)
        update(st, mid + 1, b, x, val, 2 * node + 2)


def getsum(st, a, b, l, r, node):
    if b < l or r < a:
        return 0
    if l <= a and b <= r:
        return st[node]
    mid = (a + b) // 2
    return getsum(st, a, mid, l, r, 1 + 2 * node) + getsum(
        st, 1 + mid, b, l, r, 2 + 2 * node
    )


def dfs2(curr, parent, start, end, cnt, res, d, arr):
    res[cnt[0]] = arr[curr - 1]
    start[curr] = cnt[0]
    cnt[0] += 1
    for i in d[curr]:
        if i != parent:
            dfs2(i, curr, start, end, cnt, res, d, arr)
            cnt[0] += 1
    res[cnt[0]] = arr[curr - 1]
    end[curr] = cnt[0]


"""-------------------Subtree queries problem on cses
def main():
    t = 1
    #t = inpu()
    for _ in range(t):
        n,q = sep()
        arr = lis()
        d = defaultdict(list)
        for i in range(n-1):
            a,b = sep()
            d[a].append(b)
            d[b].append(a)
        res = [0]*(2*n)
        start = defaultdict(int)
        end = defaultdict(int)
        cnt = [0]
        dfs2(1,-1,start,end,cnt,res,d,arr)
        print(res)
        st=[0]*(4*(len(res)))
        build(0,len(res)-1,st,res,0)
        #print(st)
        for i in range(q):
            l = lis()
            if l[0]==1:
                p,q = start[l[1]],end[l[1]]
                diff = l[2] - res[p]
                res[p] = l[2]
                diff2 = l[2] - res[q]
                res[q] = l[2]
                update(st,0,len(res)-1,p,diff,0)
                update(st,0,len(res)-1,q,diff2,0)
            else:
                p,q = start[l[1]],end[l[1]]
                print(getsum(st,0,len(res)-1,p,q,0)//2)
"""
"""def build2(a,b,st,arr,node,s):
    if a==b:
        s.add(arr[a-1])
        st[node] = len(s)
        return s
    mid = (a+b)//2
    p = build2(a,mid,st,arr,2*node+1,s)
    q = build2(mid+1,b,st,arr,2*node+2,s)
    #print(p,q)
    p.union(q)
    st[node] = len(p)
    return p
def ans(a,b,st,l,r,node):
    if l>b or r<a:
        return 0
    if l<=a and r>=b:
        return st[node]
    mid=(a+b)//2
    return ans(a,mid,st,l,r,2*node+1)+ans(mid+1,b,st,l,r,2*node+2)"""


def main():
    t = 1
    t = inpu()
    for _ in range(t):
        n, k = sep()
        arr = lis()
        arr.sort()
        ans = sum(arr[: n - 2 * k])
        p = arr[n - 2 * k :]
        c = Counter(p)
        max1 = 0
        for i in c:
            max1 = max(max1, c[i])
        res = max(0, (2 * max1 - 2 * k) // 2)
        print(ans + res)


if __name__ == "__main__":
    """
    threading.stack_size(2 * 10 ** 8)
    threading.Thread(target=main).start()
    """
    main()
