from sys import stdin

input = stdin.readline


def answer():

    for i in range(1, 1 + n):
        if i not in b:
            root = i
            break

    for i in range(1, 1 + n):
        if i == root:
            continue
        print(root, i)


for _ in range(int(input())):
    n, m = map(int, input().split())

    b = set()
    for _ in range(m):
        u, v, w = map(int, input().split())

        b.add(v)

    answer()
