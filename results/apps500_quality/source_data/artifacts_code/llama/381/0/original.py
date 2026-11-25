import sys

def build_graph(k):
    if k == 1:
        print("YES")
        print("2 1")
        print("1 2")
    elif k % 2 == 0:
        print("YES")
        n = k + 1
        m = (n - 1) * k // 2
        print(n, m)
        for i in range(1, n):
            for j in range(i + 1, n):
                if i != j:
                    print(i + 1, j + 1)
        print(n, n + 1)
    else:
        print("NO")

k = int(input())
build_graph(k)
