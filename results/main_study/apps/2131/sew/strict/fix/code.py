# python3


def readline(): return  tuple(map(int, input().split()))

def readlines(count): return  (readline() for  __ in  range(0, count))

def main():
    n,=readline()
    degree, root = [0] * n, None
    for  (a, b) in  readlines(n-1):
        degree[a-1]+=1
        degree[b-1]+=1

    for  (x, d) in  enumerate(degree, start=1):
        if d > 2:
            if root is not None:
                print("No")
                return
            else:
                root = x

    if  root is  None:
        root=1

    ways=[i for (i, d) in enumerate(degree, start=1) if d == 1 and i != root]
    print("Yes")
    print(len(ways))
    print("\n".join(map(f"{root} {{}}".format, ways)))


main()
