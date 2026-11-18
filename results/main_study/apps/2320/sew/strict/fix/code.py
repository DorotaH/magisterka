from collections import *


def go():
 n,s,t=int(input()),input(),input()
 if Counter(s)!=Counter(t): return  -1
 ans=0
 for  i in  range(0, n):
  k = 0
  for j in range(i,n):
   while n>k and t[j] != s[k]: k += 1
   if  k == n: break
   k += 1
   ans = max(ans, j - i + 1)
 return  n-ans
for  _ in  range(int(input())):
 print(go())
