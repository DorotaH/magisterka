def INV(a, m) :
    m0 = m
    y = 0
    x=1 
    if  (1 == m) :
        return 0 
    while  (a > 1) : 
        q=a//m 
        t=m 
        m=a%m
        a=t
        t=y 
        y=x-(q * y)
        x=t
    if  (x<0) :
        x += m0 
    return x
def GCD(a, b):
  if  0 == a: return b
  return GCD(b % a,a)
def solve():
  n, m, x, y, vx, vy=list(map(int, input().split()))
  if  0 == vx:
    if x != 0 and n != x:
      print("-1")
      return 0
    ans=[0,0]
    ans[0]=x
    if vy<0: ans[1]=0
    else: ans[1]=m
    print(ans[0],ans[1])
    return 0
  if  0 == vy:
    if y != 0 and m != y:
      print("-1")
      return 0
    ans=[0,0]
    ans[1]=y
    if vx<0: ans[0]=0
    else: ans[0]=n
    print(ans[0],ans[1])
    return 0
  if  vx==-1 and  0 == x: vx=1
  if  1 == vx and  x == n: vx=-1
  if  vy==-1 and  0 == y: vy=1
  if  1 == vy and  y == m: vy=-1
  g = GCD(n,m)
  m1 = n
  m2=m
  a1 = -1 * vx * x % m1
  a2 = -1 * vy * y % m2
  if  a1%g!=a2%g:
    print("-1")
    return 0
  if GCD(m1//g,m2) == 1:
    m1 = m1 // g
  else:
    m2 = m2 // g
  m1_bar = INV(m2,m1)
  m2_bar = INV(m1,m2)
  k=((a1 * m1_bar*m2)+(a2 * m2_bar*m1))%(m1*m2)
  rowtouch = ((k+m-1)//m) % 2
  coltouch = ((k+n-1)//n) % 2
  ans=[0,0]
  if  1 == vx: ans[0]=0
  else: ans[0] = n
  if  1 == vy: ans[1]=0
  else: ans[1] = m
  if  1 == rowtouch: ans[1]=m-ans[1]
  if  1 == coltouch: ans[0]=n-ans[0]
  print(ans[0],ans[1])
  return 0
solve()