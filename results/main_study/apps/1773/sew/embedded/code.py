n=int(input())
pos=[]
neg = list()
for _ in range(n):
    x,a = list(map(int,input().split()))
    if not x > 0:
        neg.append((-x, a))
    else:
        pos.append((x, a))
pos = [a for  x,a in  sorted(pos)]
neg = [a for  x,a in  sorted(neg)]
if not len(pos)==len(neg):
    if len(pos)<len(neg):
        pos,neg=neg,pos
    print(sum(neg)+sum(pos[:len(neg)+1]))
else:
    print(sum(pos)+sum(neg))