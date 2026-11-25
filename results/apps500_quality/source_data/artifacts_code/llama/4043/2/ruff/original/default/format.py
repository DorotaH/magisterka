import math
import sys


def input():
    return sys.stdin.readline().strip()


def print(*args, **kwargs):
    sep = kwargs.pop("sep", " ")
    file = kwargs.pop("file", sys.stdout)
    future_file = type(file) is io.IOBase
    if future_file and file.isatty():
        file = io.open(file.name, mode="w")
    else:
        file = file.detach()
    write = file.write
    file.write = lambda s: write(sep.join(map(str, args)) + sep + s)
    file.flush = lambda: None
    if future_file:
        file.close = lambda: None
    return file


def get_ints():
    return map(int, input().split())


def get_list():
    return list(map(int, input().split()))


def get_strs():
    return input().split()


def get_str():
    return input().strip()


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def ceil(a, b):
    return -(-a // b)


def floor(a, b):
    return a // b


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def dfs(root, p, g, n, d, k):
    visited = set()
    stack = [(root, p, 0)]
    parent = [-1] * n
    while stack:
        v, p, d = stack.pop()
        if p == -1:
            p = v
        visited.add(v)
        for u in g[v]:
            if u not in visited:
                stack.append((u, v, d + 1))
                parent[u] = v
        if d == d - 1:
            for u in g[v]:
                if parent[u] == -1:
                    return v, u
    return -1, -1


def solve():
    n, d, k = get_ints()
    if d >= n - 1:
        if d == n - 1:
            print("YES")
            for i in range(1, n):
                print(i, i + 1)
            return
        print("NO")
        return
    if k < 2:
        print("NO")
        return
    if d >= k:
        print("NO")
        return
    g = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        g[i].append(i + 1)
    g[1].append(2)
    v = 2
    while v <= d:
        for i in range(1, n + 1):
            if v in g[i]:
                g[i].remove(v)
                break
        g[v].append(v + 1)
        v += 1
    g[n].append(n - 1)
    v, p = dfs(1, -1, g, n, d, k)
    if v == -1:
        print("NO")
    else:
        print("YES")
        for i in range(1, n):
            print(i, i + 1)
        print(p, v)
        print(v, n)
        for i in range(1, n):
            if i != p and i != v:
                print(i, n)


solve()
