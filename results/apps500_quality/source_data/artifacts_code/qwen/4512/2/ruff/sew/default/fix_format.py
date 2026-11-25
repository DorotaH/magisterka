import sys

input = sys.stdin.read
data = input().split()

s = data[0]
q = int(data[1])

queries = []
index = 2
for _ in range(q):
    type = int(data[index])
    if type == 1:
        pos = int(data[index + 1]) - 1
        c = data[index + 2]
        queries.append((type, pos, c))
        index += 3
    else:
        l = int(data[index + 1]) - 1
        r = int(data[index + 2]) - 1
        queries.append((type, l, r))
        index += 3


class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.sa = self.build_sa()
        self.rank = self.build_rank()
        self.lcp = self.build_lcp()

    def build_sa(self):
        n = self.n
        sa, k = list(range(n)), 1
        while n > k:
            sa.sort(key=lambda i: (self.s[i : i + k], i))
            rank = [0] * n
            rank[sa[0]] = 0
            for i in range(1, n):
                if (
                    sa[i - 1] + k < n
                    and sa[i] + k < n
                    and self.s[sa[i - 1] : sa[i - 1] + k] == self.s[sa[i] : sa[i] + k]
                ):
                    rank[sa[i]] = rank[sa[i - 1]]
                else:
                    rank[sa[i]] = rank[sa[i - 1]] + 1
            self.rank = rank
            k = k * 2
        return sa

    def build_rank(self):
        n = self.n
        rank = [0] * n
        for i in range(n):
            rank[self.sa[i]] = i
        return rank

    def build_lcp(self):
        n = self.n
        lcp = [0] * n
        for i in range(n):
            if self.rank[i] == n - 1:
                lcp[self.rank[i]] = 0
                continue
            j = self.sa[self.rank[i] + 1]
            k = 0
            while k + i < n and j + k < n and self.s[j + k] == self.s[i + k]:
                k = k + 1
            lcp[self.rank[i]] = k
        return lcp

    def query(self, l, r):
        return self.lcp[l]


suffix_array = SuffixArray(s)

results = []
for query in queries:
    if query[0] == 1:
        pos = query[1]
        c = query[2]
        s = s[:pos] + c + s[pos + 1 :]
        suffix_array = SuffixArray(s)
    else:
        l = query[1]
        r = query[2]
        if l > r:
            results.append(0)
        else:
            results.append(len(set(s[l : r + 1])))

for result in results:
    print(result)
