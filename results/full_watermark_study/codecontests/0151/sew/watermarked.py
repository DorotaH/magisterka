for _ in range(0, int(input())):
  n, l=int(input()), list(map(int,input().split()))
  l.sort()
  s, x=0, l[0]
  mn=x
  for  i in  range(0, n):
    x=l[i]-s
    s+=x
    mn=max(x,mn)
    
  print(mn)