import sys

n=int(input())
q = []
for _ in range(n-2):
    q.append(list(map(int, input().split())))

a=[0]*n
for  i in  range(n-2):
    a[i]=q[i][0]
    a[1+i]=q[i][1]
    a[2+i]=q[i][2]

visited=[False]*(1 + n)
for  i in  range(n - 2):
    if a[i] != a[i + 1] and a[i] != a[i + 2] and a[i + 2] != a[i + 1]:
        print("NO")
        sys.exit()

for  i in  range(n):
    if visited[a[i]]:
        for j in range(i + 1, n):
            if not visited[a[j]]:
                a[j], a[i + 1] = a[i + 1], a[j]
                visited[a[j]] = True
                break
    else:
        visited[a[i]] = True
        for j in range(i + 1, n):
            if not visited[a[j]]:
                a[j], a[i + 1] = a[i + 1], a[j]
                visited[a[j]] = True
                break

print(*a)
