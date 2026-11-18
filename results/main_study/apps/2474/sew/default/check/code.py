mod=7 + 10**9


def power(p, e):
  ret=1
  while(e):
    if(e&1):
      ret = ret * p
      ret = ret % mod
    p*=p
    e >>= 1
  return  ret

N, C = int(input()), list(map(int, input().split()))
C.sort()

f=0
for  i in  range(N):
  f+=(N-i+1)*C[i]
  f%=mod

f*=power(2, N - 1)**2%mod
f%=mod
print(f)