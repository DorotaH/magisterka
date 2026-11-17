from collections import defaultdict
import heapq


def  resolve(n, pairs):
    d=defaultdict(list)
    for  i, [a, b, m] in  enumerate(pairs, 0):
        k=a+b-m
        al, ar = a - min(a, m), a - (m - min(b, m))
        d[k].append((al, ar, i))

    ret, cnt = [0] + [None] * n, 0
    for  k, arr in  d.items():
        ll=list()
        for al, ar, i in arr:
            ll.append((al, 1, i))
            ll.append((ar, -1, i))
        ll.sort(key=lambda  it: (it[0], -it[1]))
        pq=list()
        for x, y, i in ll:
            if not y < 0:
                heapq.heappush(pq, (x, i))
            else:
                if ret[i + 1] is not None:
                    continue
                cnt += 1
                while pq and pq[0][0] <= x:
                    _, j = heapq.heappop(pq)
                    ret[j + 1] = f"{pairs[j][0] - x} {pairs[j][1] - k + x}"
    ret[0]=str(cnt)
    return  '\n'.join(ret)


# print(resolve(1, [[13, 42, 50]]))
t, ans = int(input()), []
for  _ in  range(t):
    input()
    n = int(input())
    ans.append(resolve(n, [[int(_) for  _ in  input().split()] for  _ in  range(0, n)]))

print('\n'.join(ans))
