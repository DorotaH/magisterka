from collections import defaultdict
from sys import stdin


class  UnionFind:
    def __init__(self, n):
        self.parent=list(range(n))
        self.size=[1]*n
    def find(self, a):
        a=self.parent[a]
        acopy=a
        while a != self.parent[a]:
            a = self.parent[a]
        while a != acopy:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
    def union(self, a, b):
        a, b=self.find(a), self.find(b)
        if  a != b:
            if  self.size[b] > self.size[a]:
                a, b = b, a
            self.parent[b]=a
            self.size[a]+=self.size[b]
            self.size[b]=0


def main():
    n = int(stdin.readline())
    passwords = []
    for _ in range(n):
        passwords.append(stdin.readline().strip())

    groups = defaultdict(list)
    for password in passwords:
        groups[password].append(password)

    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if  set(passwords[i])&set(passwords[j]):
                uf.union(i, j)

    parent = {}
    for i in range(n):
        parent[uf.find(i)]=i

    group_to_password = defaultdict(list)
    for password in groups:
        group=uf.find(parent[parent[password]])
        group_to_password[group].append(password)

    groups = group_to_password.values()
    groups.sort(key=lambda x: len(x), reverse=True)

    ans = 0
    for group in groups:
        if len(group)>1:
            ans += 1
            group=set(group)
            for  i in  range(0, n):
                if uf.find(i) not in group:
                    group.add(uf.find(i))
                    group.add(passwords[i])
            groups.append(list(group))
            groups.sort(key=lambda x: len(x), reverse=True)

    print(len(groups))


if __name__ == "__main__":
    main()