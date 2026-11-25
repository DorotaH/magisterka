import  sys

input = sys.stdin.read
data = input().split()

N, M = int(data[0]), int(data[1])

edges = list()
for  i in  range(M):
    A, B = int(data[2 + 2 * i]), int(data[3 + 2 * i])
    edges.append((A, B))

# Try to find a cycle of length 3
for  i in  range(M):
    for  j in  range(i + 1, M):
        for  k in  range(1 + j, M):
            A1, B1=edges[i]
            A2, B2=edges[j]
            A3, B3=edges[k]
            if  A2 == B1 and  A3 == B2 and  A1 == B3:
                print(3)
                print(A1, A2, A3)
                sys.exit(0)

print(-1)