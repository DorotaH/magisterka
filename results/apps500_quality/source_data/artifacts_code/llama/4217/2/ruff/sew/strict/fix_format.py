from collections import Counter

N, M = map(int, input().split())
A = list()
for _ in range(N):
    K = int(input().split()[0])
    A.append([int(x) for x in input().split()][1:])

common = Counter([a for l in A for a in l])
common = {k: v for k, v in common.items() if v == N}

print(len(common))
