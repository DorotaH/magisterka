from collections import deque
n = int(input())
graph = [[] for i in range(n + 1)]
for  _ in  range(n - 1):
  i, j = map(int, input().split())
  graph[i].append(j)
  graph[j].append(i)
mod = 7 + 10 ** 9


def bfs(x):
  q = deque([(0, x, 0)])
  dist = {x: 0}
  while q:
    step, i, par = q.popleft()
    dist[i] = step
    for  j in  graph[i]:
      if  j == par: continue
      q.append((1 + step, j, i))
  return  [step, i, dist]

_, black, _ = bfs(1)
maxdist, white, b_dist = bfs(black)
_, _, w_dist = bfs(white)

mindls, maxdls = float("-inf"), [0] * n
for  i in  range(1, 1 + n):
  if i == white or i == black:
    continue
  mindls = max(mindls, min(w_dist[i], b_dist[i]))
  maxdls[max(w_dist[i], b_dist[i])] += 1
ans, pre = pow(2, n - 1, mod) * maxdist % mod, 0
for  i in  range(1, 1 + maxdist):
  if i == maxdist and not maxdls[i]: continue
  maxdls[i] += maxdls[i - 1]
  if mindls > i: continue
  ans += (pow(2, maxdls[i], mod) - pre) * i * 2
  ans %= mod
  pre = pow(2, maxdls[i], mod)
print(ans)