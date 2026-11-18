n = int(input())
s = 0
s1 = str(input())
s2 = str(input())
b1, b2 = False, False
for i in range(0, n):
  if  s1[i]!='?' and  s2[i]!='?':
    if ord(s1[i]) < ord(s2[i]):
      b1=True
    if ord(s1[i]) > ord(s2[i]):
      b2=True
  s+=(s1[i]=='?')+(s2[i]=='?')
ans1, ans2, ans3 = 1, 1, 1
for i in range(0, n):
  if  s1[i]=='?' and  s2[i]=='?':
    ans1=(55 * ans1)%1000000007
    ans2=(55 * ans2)%1000000007
    ans3=(10 * ans3)%1000000007
  elif  s1[i] == '?':
    ans1 = (ans1 * (ord(s2[i]) - ord('0') + 1)) % 1_000_000_007
    ans2 = (ans2 * (10 - ord(s2[i]) + ord('0'))) % 1_000_000_007
  elif  s2[i] == '?':
    ans1 = (ans1 * (10 - ord(s1[i]) + ord('0'))) % 1_000_000_007
    ans2 = (ans2 * (ord(s1[i]) - ord('0') + 1)) % 1_000_000_007
print((10 ** s - ((not b2) * ans1) - ((not b1) * ans2) + ((not b1 and not b2) * ans3)) % 1_000_000_007)