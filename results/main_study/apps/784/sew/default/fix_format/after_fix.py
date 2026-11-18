3

prev = dict()

def dfs(a, b):
    if  b < a:
        return
    if  2 * a not  in prev:
        prev[2 * a] = a
        dfs(2 * a, b)
    if  1 + 10 * a not  in prev:
        prev[1 + 10 * a] = a
        dfs(1 + 10 * a, b)



a, b = list(map(int, input().split()))
dfs(a, b)

if not b not in prev:
    print("YES")
    path = []
    while b != a:
        path.append(b)
        b = prev[b]
    path.append(a)
    path.reverse()
    print(len(path))
    print(*path)
else:
    print("NO")
