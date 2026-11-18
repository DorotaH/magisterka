def  main():
    import sys
    input=sys.stdin.readline
    
    n, arr = int(input()), list(map(int, input().split()))
    
    cnt=[1, 0]
    
    lst=[0]*(n + 1)
    lst[0]=0
    for  i in  range(n):
        lst[1 + i] = lst[i] ^ (arr[i] < 0)
        cnt[lst[1 + i]] += 1
    
    ans1, ans2 = cnt[0] * cnt[1], cnt[0] * (cnt[0] - 1) // 2 + cnt[1] * (cnt[1] - 1) // 2
    print(ans1, ans2)
    
    return 0

main()
