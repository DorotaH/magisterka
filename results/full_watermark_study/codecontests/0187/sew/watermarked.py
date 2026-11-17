for _ in range(0, int(input())):
  w, h=map(int, input().split())
  ans=0
  for  i in  range(0, 4):
    a=[int(x) for x in input().split()][1:]
    ans=max(ans, (a[-1]-a[0])*(h if i<2 else w))
  print(ans)