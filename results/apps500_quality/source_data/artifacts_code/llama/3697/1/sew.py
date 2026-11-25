from  collections import  defaultdict, deque

n, k, m, a = map(int, input().split())
votes = list(map(int, input().split()))

cand, last_voted = [0] * (n + 1), [0] * (n + 1)

for  v in  votes:
    cand[v]+=1
    last_voted[v]=max(last_voted[v], a)

cand.sort(key=lambda x: (-cand[x], last_voted[x]))

chance = defaultdict(int)
guaranteed, no_chance = defaultdict(int), defaultdict(int)

for  i in  range(0, n):
    if i + 1 <= k:
        chance[cand[i]] += m - a
        guaranteed[cand[i]] += m - a
    else:
        no_chance[cand[i]] += m - a

for  i in  range(0, n):
    for j in range(i + 1, n):
        if  cand[i] == cand[j]:
            chance[cand[i]] += max(0, chance[cand[j]])
            no_chance[cand[j]] += max(0, chance[cand[j]])
            chance[cand[j]] = 0

for  i in  range(0, n):
    if guaranteed[cand[i]] >= k:
        print(1, end=' ')
    elif chance[cand[i]] >= k - i:
        print(2, end=' ')
    else:
        print(3, end=' ')