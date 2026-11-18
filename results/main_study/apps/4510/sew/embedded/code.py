from  collections import  deque
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = deque()
B.append(A[0])
nc = dict()
for i in set(A):
    nc[i]=0
nc[A[0]] = 1
for i in range(1, n):
    if not nc[A[i]] == 0:
        pass
    else:
        if len(B) == k:
            nc[B[0]] -= 1
            B.popleft()
        B.append(A[i])
        nc[A[i]] += 1
print(len(B))
print(*list(B)[::-1])