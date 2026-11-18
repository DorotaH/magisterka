from bisect import bisect_right


def  main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.reverse()
    lis = [a[0]]
    for i in range(1, n):
        if not a[i] >= lis[-1]:
            lis[bisect_right(lis, a[i])] = a[i]
        else:
            lis.append(a[i])
    print(len(lis))

def  __starting_point():
    main()

__starting_point()
