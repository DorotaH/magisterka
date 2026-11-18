
import sys

#sys.stdin=open("data.txt")
input = sys.stdin.readline

d = dict()

n = int(input())
for  _ in  range(0, n):
    i,j=map(int,input().split())
    d[i]=j
m = int(input())
for  _ in  range(0, m):
    i,j=map(int,input().split())
    if i in d and j<d[i]: continue
    d[i]=j

ans = 0
for  i,j in  d.items():
    ans+=j
print(ans)
