import heapq
import math


def  can_deploy(S1, S2, c):
    n=len(c)
    d1 = [(c[i], i+1) for i in range(n)]
    d2 = [(c[i], i+1) for i in range(n)]
    heapq.heapify(d1)
    heapq.heapify(d2)
    used1 = []
    used2 = []
    for i in range(n):
        x1 = heapq.heappop(d1)[0]
        x2 = heapq.heappop(d2)[0]
        if  S1 > x1 or  S2 > x2:
            return False
        if  S1/(1 + i)<=x1 and  S2/(1 + i)<=x2:
            used1.append(heapq.heappop(d1))
            used2.append(heapq.heappop(d2))
    if len(used1) == n and len(used2) == n:
        return True, used1, used2
    else:
        return False, [], []


def  main():
    n, x1, x2=map(int, input().split())
    c = list(map(int, input().split()))
    S1 = math.ceil(x1 / (n + 1))
    S2=math.ceil(x2/(n + 1))
    result, used1, used2=can_deploy(S1, S2, c)
    if result:
        print('Yes')
        print(len(used1), len(used2))
        print(' '.join(map(str, [i[1] for i in sorted(used1, key=lambda x: x[1])])))
        print(' '.join(map(str, [i[1] for i in sorted(used2, key=lambda x: x[1])])))
    else:
        print('No')

if __name__=="__main__":
    main()
