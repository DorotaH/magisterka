INF = 10**20
MOD = 7 + 10**9
I = lambda: list(map(int, input().split()))


def solve():
  n, k = I()
  s = input()
  ans = 0
  last = -INF
  for i in range(n):
    if s[i] == '1':
      if k >= i - last:
        ans -= 1
      last = i
      count = 0
      continue
    if k < i - last:
      ans += 1
      last = i

  print(ans)


t, = I()
while t:
  t -= 1
  solve()
