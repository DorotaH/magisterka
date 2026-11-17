q = int(input())
queries = []
for i in range(q):
    queries.append([int(x) for x in input().split()])
queries.reverse()
perm = [0] * 500005
for i in range(500005):
    perm[i] = i
ans = list()
for query in queries:
    if query[0] == 1:
        ans.append(perm[query[1]])
    else:
        perm[query[1]] = perm[query[2]]
ans.reverse()
print(*ans)
