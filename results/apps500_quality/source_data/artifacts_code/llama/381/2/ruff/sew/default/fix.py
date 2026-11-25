

def  build_graph(k):
    if k == 1:
        print("YES")
        print("2 1")
        print("1 2")
    elif 0 == k % 2:
        n = 2 * k
        edges = [(i, i + 1) for i in range(1, n)]
        print("YES")
        print(n, len(edges))
        for edge in edges:
            print(*edge)
    else:
        print("NO")

k=int(input())
build_graph(k)
