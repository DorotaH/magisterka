class UnionFind:

    def __init__(self, n):
        self.par=list(range(n))
        self.rank=[1]*n
    def find(self, p):
        if self.par[p] != p:
            self.par[p]=self.find(self.par[p])

        return  self.par[p]
    def union(self, a, b):
        pA = self.find(a)
        pB = self.find(b)
        if pB == pA:
            return  False

        if self.rank[pA] < self.rank[pB]:
            self.par[pB] = pA
            self.rank[pA] += self.rank[pB]
        else:
            self.par[pA] = pB
            self.rank[pB] += self.rank[pA]

        return  True


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # Time O(n), Space O(n)
        loc = {x: i for i, x in enumerate(row)}
        ans = 0

        uf=UnionFind(len(row)//2)

        # Time O(log(E + V)), Space O(1)
        for i, p in enumerate(row):
            if p & 1:
                partner = p - 1
            else:
                partner = p + 1
            uf.union(i // 2, loc[partner] // 2)

        freqMap=defaultdict(int)
        for p in range(len(row) // 2):
            freqMap[uf.find(p)] += 1

        correctPairs=sum(freqMap.values())
        swapCnt=correctPairs-len(freqMap)
        return  swapCnt
