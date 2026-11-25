import sys

def  solve():
    n, m=map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    for  i in  range(n):
        row=[]
        for  j in  range(m):
            k = 1
            for x in a[i]:
                k=max(k, x)
            row.append(k)
        print(*row)

if __name__ == "__main__":
    solve()