import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

edges = []
for i in range(M):
    A = int(data[2 + 2 * i])
    B = int(data[3 + 2 * i])
    edges.append((A, B))

# Try to find a cycle of length 3
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            A1, B1 = edges[i]
            A2, B2 = edges[j]
            A3, B3 = edges[k]
            if B1 == A2 and B2 == A3 and B3 == A1:
                print(3)
                print(A1, A2, A3)
                sys.exit(0)

print(-1)
