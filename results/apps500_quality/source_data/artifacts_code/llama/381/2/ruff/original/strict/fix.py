
def build_graph(k):
    if k == 1:
        print("YES")
        print("2 1")
        print("1 2")
    elif k % 2 == 0:
        n = 2 * k
        edges = []
        for i in range(1, n):
            edges.append((i, i + 1))
        print("YES")
        print(n, len(edges))
        for edge in edges:
            print(*edge)
    else:
        print("NO")

k = int(input())
build_graph(k)
