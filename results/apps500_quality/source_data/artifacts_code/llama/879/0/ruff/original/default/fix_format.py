n = int(input())
p = [0] + list(map(int, input().split()))

parent = [i for i in range(n + 1)]
stack = []

for i in range(n, 1, -1):
    parent[p[i]] = parent[i]
    stack.append(i)

print(1, end=" ")
while stack:
    x = stack.pop()
    print(x, end=" ")
    x = parent[x]
    print(x, end=" ")
