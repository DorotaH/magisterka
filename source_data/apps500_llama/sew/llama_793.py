import  sys

def  solve():
    n, arr = int(input()), list(map(int, input().split()))
    subset, total = [], sum(arr)
    if total % 2 == 0:
        print(len(arr))
        for i in range(n):
            print(i + 1, end=' ')
        print()
    else:
        missing = n - (total - arr[0])
        if missing % 2 == 0:
            print(1)
            print(1)
        else:
            print(2)
            print(1, n)

t = int(input())
for _ in range(t):
    solve()