from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, i):
        node = self.root
        for c in s:
            node = node.children[c]
        node.count += 1

    def query(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count


class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.trie = Trie()
        self.n = len(s)
        self.lcp = [0] * self.n
        self.build()

    def build(self):
        self.suff = sorted((s[i:] for i in range(self.n)))
        for i in range(self.n):
            self.lcp[i] = self.n - self.suff[i].find(self.suff[i][-1])
        for i in range(self.n):
            self.trie.insert(self.suff[i], i)
        self.sa = sorted(range(self.n), key=lambda i: self.suff[i])
        self.tree = [0] * (4 * self.n)
        self.build_tree(0, 0, self.n - 1)

    def build_tree(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = self.lcp[tl]
        else:
            tm = (tl + tr) // 2
            self.build_tree(2 * v + 1, tl, tm)
            self.build_tree(2 * v + 2, tm + 1, tr)
            self.tree[v] = max(self.tree[2 * v + 1], self.tree[2 * v + 2])

    def update(self, i, x):
        i = self.sa[i]
        self.lcp[i] = max(self.lcp[i], x)
        self.trie.insert(self.suff[i], i)
        self.update_tree(0, 0, self.n - 1, i)

    def update_tree(self, v, tl, tr, i):
        if tl == tr:
            self.tree[v] = self.lcp[i]
        else:
            tm = (tl + tr) // 2
            if i <= tm:
                self.update_tree(2 * v + 1, tl, tm, i)
            else:
                self.update_tree(2 * v + 2, tm + 1, tr, i)
            self.tree[v] = max(self.tree[2 * v + 1], self.tree[2 * v + 2])

    def query(self, l, r):
        l, r = self.sa[l], self.sa[r]
        res = max(self.lcp[l], self.lcp[r])
        l >>= 1
        r >>= 1
        while l != r:
            if l > r:
                res = max(res, self.tree[2 * l + 1])
                l = (l << 1) | 1
            else:
                res = max(res, self.tree[2 * r + 2])
                r = (r << 1) | 1
        return res


def main():
    s = input()
    sa = SuffixArray(s)
    q = int(input())
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            pos, c = int(query[1]) - 1, query[2]
            sa.update(pos, 0)
            s = list(s)
            s[pos] = c
            sa = SuffixArray("".join(s))
        else:
            l, r = int(query[1]) - 1, int(query[2]) - 1
            print(sa.query(l, r))


if __name__ == "__main__":
    main()
