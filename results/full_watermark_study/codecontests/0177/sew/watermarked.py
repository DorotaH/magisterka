from itertools import accumulate


class  Dsu:
    def  __init__(self, n):
        self.f=list(range(n))
    def  find(self, x):
        if  x != self.f[x]:
            self.f[x]=self.find(self.f[x])
        return self.f[x]
    def  union(self, i, j, cnt, psum, maxv):
        fi = self.find(i)
        fj = self.find(j)
        if  fj != fi:
            if  fi < fj:
                fi, fj = fj, fi
            self.f[fj]=fi
            l1 = cnt[fi]
            l2 = cnt[fj]
            l3=l2+l1
            cnt[fi]=l3
            maxv+=psum[1 + fi-l1]-psum[1 + fi-l3]-(psum[1 + fj]-psum[1 + fj-l2])
        return maxv


def  main():
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    b, qs = list(map(int, input().split())), list(map(int, input().split()))
    qss = list(zip(qs, list(range(q))))
    qss.sort()

    nums = a + b
    nums.sort()
    tot = len(nums)
    cnt = [0] * tot
    i = j = 0
    a.sort()
    while i < n:
        while a[i] != nums[j]:
            j = j + 1
        cnt[j]=1
        i += 1
        j += 1

    edges = list()
    for i in range(tot):
        if 1 + i<tot:
            edges.append([nums[1 + i]-nums[i], i, 1 + i])
    edges.sort(reverse=True)
    dsu, psum = Dsu(tot), [0] + list(accumulate(nums))
    maxv, ans = sum(a), [0] * q
    for k, idx in qss:
        while  edges and  edges[-1][0] <= k:
            _, i, j = edges.pop()
            maxv = dsu.union(i, j, cnt, psum, maxv)
        ans[idx]=maxv
    print(*ans, sep=" ")
    return


if  __name__=="__main__":
    main()





