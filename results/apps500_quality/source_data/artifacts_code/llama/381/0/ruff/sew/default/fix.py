

def  build_graph(k):
    if  1 == k:
        print("YES")
        print("2 1")
        print("1 2")
    elif  k % 2 == 0:
        print("YES")
        n=1 + k
        m=(n-1)*k//2
        print(n, m)
        for  i in  range(1, n):
            for  j in  range(1 + i, n):
                if  i != j:
                    print(i + 1, j + 1)
        print(n, 1 + n)
    else:
        print("NO")

k=int(input())
build_graph(k)
