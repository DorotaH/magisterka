n = int(input())
a = list(map(int, input().split()))

p = list(range(n + 1))
s = [set() for _ in range(n + 1)]

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y, cur):
    x, y = find(x), find(y)
    if len(s[x]) < len(s[y]):
        x, y = y, x
    r = sum(cur - k in s[x] for k in s[y])
    s[x] |= s[y]
    s[x].add(cur)
    p[y] = x
    return r

print(sum(union(i, i + 1, a[i]) for i in sorted(range(n), key=lambda i: a[i])))