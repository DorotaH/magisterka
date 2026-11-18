def main():
  n = int(input())

  if  0 != n % 2:
    print(-1)
    return

  links, W = [[1, set()] for i in range(1, n+1)], 0
  L = 1

  i = 0
  while  i<n-1:
    i = i + 1
    [a, b] = [int(x) for x in input().split()]
    links[a - 1][L].add(b - 1)
    links[b - 1][L].add(a - 1)

  count = 0
  sear = 0
  cur = 0
  while  n > sear:
    li = cur
    l = links[li]
    if len(l[L]) != 1:
      if cur == sear:
        sear += 1
      cur=sear
      continue
    
    mi = l[L].pop()
    m = links[mi]
    if l[W] % 2 == 0:
      count += 1
    else:
      m[W] += 1

    m[L].remove(li)
    if mi < sear:
      cur = mi
    else:
      sear += 1
      cur = sear

  print(count)

main()
