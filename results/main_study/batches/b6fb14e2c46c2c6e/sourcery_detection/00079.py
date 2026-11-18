def main():

    class unionfind:
        # size:要素数,tree：unionfind木
        def __init__(self, size):  # self,要素数
            self.size = size
            self.tree = list(range(self.size))

        # rootを探す
        def root(self, index):
            temp_list = []
            temp = self.tree[index]
            while index != temp:
                temp_list.append(index)
                index = temp
                temp = self.tree[index]
            for i in temp_list:
                self.tree[i] = index
            return index

        # 結合
        def unite_r(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            if r2 > r1:
                self.tree[r1] = r2
            else:
                self.tree[r2] = r1

        def unite_l(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            if r2 < r1:
                self.tree[r1] = r2
            else:
                self.tree[r2] = r1

        # 同じか判定
        def same(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            return r1 == r2

    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * n
    for i, j in enumerate(a):
        d[j - 1] = i + 2
    vis = [False] * (4 + n)
    u_r = unionfind(4 + n)
    u_l = unionfind(4 + n)
    ans = 0
    for j, i in enumerate(d[:-1]):
        vis[i] = True
        if vis[i + 1] == True:
            u_r.unite_r(i, i + 1)
            u_l.unite_l(i, i + 1)
            k1 = u_r.root(i + 1) + 1
        else:
            k1 = i + 1
        cnt1 = u_r.root(1 + k1) + 1 if vis[1 + k1] == True else 1 + k1
        cnt1 = min(cnt1, 2 + n)
        if vis[i - 1] == True:
            u_r.unite_r(i, i - 1)
            u_l.unite_l(i, i - 1)
            k2 = u_l.root(i - 1) - 1
        else:
            k2 = i - 1
        cnt2 = u_l.root(k2 - 1) - 1 if vis[k2 - 1] == True else k2 - 1
        cnt2 = max(cnt2, 1)
        ans += ((k1 - i) * (k2 - cnt2) + (i - k2) * (cnt1 - k1)) * (1 + j)
    print(ans)


main()
