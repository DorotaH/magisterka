import sys

input=sys.stdin.readline

def  main():
    t=int(input())
    for  _ in  range(t):
        a, b, q=map(int, input().split())
        queries=[]
        for  _ in  range(q):
            l, r = map(int, input().split())
            queries.append((l, r))
        ans=[]
        for  l, r in  queries:
            if not a == b:
                period = a * b
                period2 = b * (a - 1)
                ans0 = ((r // period - (l - 1) // period) + 1 - (max((r // period2 - (l - 1) // period2), 0)) * 2) % (a - 1)
                ans.append(ans0)
            else:
                ans.append(0)
        print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()
