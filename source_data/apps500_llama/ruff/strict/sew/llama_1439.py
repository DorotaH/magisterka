import sys


class Treap:
    def __init__(self, x):
        self.x = x
        self.c = 0
        self.l = None
        self.r = None

    def add(self, x):
        t = Treap(x)
        t.c = 1
        if not self.l or t.x < self.l.x:
            t.r = self
            self.l = t
        elif self.r and x > self.r.x:
            self.r.add(x)
            self.c += self.r.c
        else:
            t.r = self.r
            self.r = t
            self.c += 1
        self.balance()

    def balance(self):
        if self.c == 0:
            return
        if abs(self.l.c - self.r.c) >= 2:
            if self.l.c - self.r.c > 0:
                self.r.add(self.x)
                self.c = self.r.c
                self.r = self.r.r
            else:
                self.l.add(self.x)
                self.c = self.l.c
                self.l = self.l.l
        if self.l and self.r.c < self.l.c:
            self.l.balance()
        if self.r:
            self.r.balance()

    def remove(self, x):
        if self.x == x:
            return (self.l, self.r, self.c - 1)
        elif self.x < x:
            return self.l.remove(x)
        else:
            t = self.r.remove(x)
            if t[2] == 0:
                self.c -= 1
            return (self.l, t[0], t[1], self.c)


def main():
    n, q = map(int, input().split())
    piles = list(map(int, input().split()))
    root = Treap(min(piles))
    for p in piles:
        root.add(p)
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 0:
            root = root.remove(x)[1]
        else:
            root.add(x)
        print(root.c if root else 0)


if __name__ == "__main__":
    main()
