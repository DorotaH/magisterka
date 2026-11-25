N = int(input())
V = list(map(int, input().split()))
T = list(map(int, input().split()))
result = list()

for i in range(N):
    evaporated = min(V[i], T[i])
    V[i] -= evaporated
    result.append(evaporated)

print(' '.join(map(str, result)))