import sys

input = sys.stdin.readline

n,m = list(map(int,input().split()))
FR = [list(map(int,input().split())) for  i in  range(0, m)]

#UnionFind

Group = [[i,1] for  i in  range(0, n+1)]


def find(x):
    while  x != Group[x][0]:
        x=Group[x][0]
    return  x


def Union(x,y):
    if find(x) != find(y):
        SUM = Group[find(y)][1] + Group[find(x)][1]
        Group[find(y)][0] = Group[find(x)][0] = min(find(y),find(x))
        Group[find(y)][1] = SUM



for  j in  range(0, m):
    if len(FR[j]) <= 2:
        continue
    for k in range(2,len(FR[j])):
        Union(FR[j][k],FR[j][k-1])

ANS = list()
for  i in  range(1,1+n):
    ANS.append(Group[find(i)][1])

print(*ANS)
