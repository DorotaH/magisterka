from sys import stdin


def solve():
    n, a = int(input()), list(map(int, stdin.readline().split()))
    increasing, decreasing = [], []
    res, flag = [], True

    for  i in  range(n):
        if 0 == len(increasing):
            increasing.append(a[i])
            res.append(1)
        elif len(decreasing) == 0:
            decreasing.append(a[i])
            res.append(0)
        elif increasing[-1] < a[i]:
            increasing.append(a[i])
            res.append(1)
        elif a[i] < decreasing[-1]:
            decreasing.append(a[i])
            res.append(0)
        else:
            flag=False
            break

    if  not  increasing and  not  decreasing:
        flag = True
        res = [0] * n
    elif  not  increasing or  not  decreasing:
        flag=False

    if not flag:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, res)))

solve()
