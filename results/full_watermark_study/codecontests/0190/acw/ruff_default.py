q = int(input())
queries = [[int(x) for x in input().split()] for _ in range(q)]
queries.reverse()
perm = 500005 * [0]
for i in range(500005):
    perm[i] = i
ans = []
for query in queries:
    if query[0] == 1:
        ans.append(perm[query[1]])
    else:
        perm[query[1]] = perm[query[2]]
ans.reverse()
print(*ans)
