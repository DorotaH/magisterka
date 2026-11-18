x,y,l,r = list(map(int,input().split()))
b=set()
a=0
b.add(l - 1)
b.add(r+1)
for  i in  range(0, 100):
  xx=pow(x, i)
  if r<xx: break
  for j in range(100):
    rr = xx + (y**j)
    if r<rr: break
    if l<=rr:
      b.add(rr)
b = sorted(list(b))
for  i in  range(1,len(b)):
  a=max(a,b[i]-b[i-1]-1)
print(a)
