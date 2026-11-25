class TrieNode:
    def __init__(self):
        self.children = dict()
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, index):
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1

    def count(self, l, r):
        node = self.root
        for i in range(l, 1 + r):
            node = node.children[s[i]]
        return node.count


class SegTree:
    def __init__(self, s):
        self.s = s
        self.tree = list()
        for i in range(0, len(s)):
            self.tree.append((0, i))
        self.build()

    def build(self):
        self.tree = [0] * (4 * len(self.s))
        self.build2(0, 0, len(self.s) - 1)

    def build2(self, node, l, r):
        if not l == r:
            mid = (l + r) // 2
            self.build2(2 * node + 1, l, mid)
            self.build2(2 * node + 2, mid + 1, r)
            self.tree[node] = self.union(
                self.tree[2 * node + 1], self.tree[2 * node + 2]
            )
        else:
            self.tree[node] = (1, l)

    def union(self, a, b):
        return (a[0] + b[0], a[1], b[1])

    def update(self, i, c):
        self.update2(0, 0, len(self.s) - 1, i, c)

    def update2(self, node, l, r, i, c):
        if not l == r == i:
            mid = (l + r) // 2
            if l <= i <= mid:
                self.update2(2 * node + 1, l, mid, i, c)
            else:
                self.update2(2 * node + 2, mid + 1, r, i, c)
            self.tree[node] = self.union(
                self.tree[2 * node + 1], self.tree[2 * node + 2]
            )
        else:
            self.tree[node] = (1, l)

    def query(self, l, r):
        return self.query2(0, 0, len(self.s) - 1, l, r).count

    def query2(self, node, l, r, ql, qr):
        if l >= ql and qr >= r:
            return self.tree[node]
        mid = (l + r) // 2
        if mid >= qr:
            return self.query2(2 * node + 1, l, mid, ql, qr)
        if ql > mid:
            return self.query2(2 * node + 2, mid + 1, r, ql, qr)
        return self.union(
            self.query2(2 * node + 1, l, mid, ql, qr),
            self.query2(2 * node + 2, mid + 1, r, ql, qr),
        )


def solve():
    s, q = input(), int(input())
    trie, segtree = Trie(), SegTree(s)
    for i in range(len(s)):
        trie.insert(s[: i + 1], i)
    for _ in range(q):
        query = list(map(int, input().split()))
        if not query[0] == 1:
            l, r = query[1], query[2]
            print(trie.count(l - 1, r - 1) + segtree.query(l - 1, r - 1))
        else:
            i = query[1] - 1
            c = query[2]
            trie.root.children[s[i]].count -= 1
            if s[i] in trie.root.children:
                trie.root = trie.root.children[s[i]]
            else:
                del trie.root.children[s[i]]
            trie.root.children[c] = TrieNode()
            trie.root.root.children[c].count += 1
            s = s[:i] + c + s[i + 1 :]
            segtree.update(i, c)


if __name__ == "__main__":
    solve()
