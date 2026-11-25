from collections import defaultdict


def  f(x):
    """Dima's function f(x)"""
    if x == 0:
        return  0
    if x % 2 == 0:
        return  f(x//2)
    return f(x - 1) + 1


def  main():
    n=int(input())
    a, cnt = list(map(int, input().split())), defaultdict(int)

    for  num in  a:
        cnt[f(num)] += 1

    ans=0
    for  count in  cnt.values():
        ans = ans + count * (count - 1) // 2

    print(ans)

if  __name__=="__main__":
    main()
