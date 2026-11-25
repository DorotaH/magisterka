from collections import defaultdict, deque


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)
        
    def add(self, i, delta):
        while i <= self.n:
            self.t[i] += delta
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.t[i]
            i -= i & -i
        return ans

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (4 * n)

    def update(self, i, val):
        i += self.n
        self.t[i] = val
        while i > 1:
            i >>= 1
            self.t[i] = max(self.t[2 * i], self.t[2 * i + 1])

    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.t[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.t[r])
            l >>= 1
            r >>= 1
        return ans

def main():
    n, k, a, b, q = map(int, input().split())
    ft = FenwickTree(n + 1)
    tree = SegmentTree(n)
    orders = defaultdict(int)
    days = deque()
    for _ in range(q):
        line = input().split()
        if line[0] == '1':
            d, a = map(int, line[1:])
            days.append((d, a))
        else:
            p = int(line[1])
            ans = 0
            for i in range(p - 1, n):
                d, a = days.popleft()
                ft.add(d, a)
                tree.update(d, a)
            for i in range(p, n):
                d, a = days.popleft()
                ft.add(d, -a)
                tree.update(d, -a)
            for i in range(p - 1, n):
                ans += ft.query(i + 1)
            if p - 1 - k >= 0:
                ans += tree.query(p - 1 - k, p - 1)
            print(ans)

if __name__ == '__main__':
    main()
