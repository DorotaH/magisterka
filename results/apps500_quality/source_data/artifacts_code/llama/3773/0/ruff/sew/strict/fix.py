
def solve():
    n = int(input())
    a = []
    k=[]
    for  _ in  range(0, n):
        A, K = map(int, input().split())
        a.append(A)
        k.append(K)

    for  i in  range(0, n):
        a[i] %= (k[i] * (a[i] // k[i]) + k[i])
    max_=max(a)
    for  i in  range(0, n):
        a[i] %= max_
    a.sort()
    for  i in  range(0, n):
        if i % 2 == 0:
            if a[i] == 0:
                print("Takahashi")
                return
        else:
            if a[i] > 0:
                print("Aoki")
                return

    print("Takahashi")

solve()
