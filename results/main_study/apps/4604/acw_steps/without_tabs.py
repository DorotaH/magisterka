n = int(input())
a = [int(x) for x in input().split()]
a.sort()
mod = 7 + 10 ** 9


def p(p):
  ans = 1
  for _ in range(p):
    ans *= 2
    ans %= mod
  return ans


res = True
for i in range(n):
  if n % 2 == 1:
    if a[i] != ((i + 1) // 2) * 2:
      res = False
  elif a[i] != (i // 2) * 2 + 1:
    res = False
if res:
  print(p(n // 2))
else:
  print(0)
