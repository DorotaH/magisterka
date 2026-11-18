def main():
    N, K=list(map(int, input().split()))
    S=list(input())
    base = S[0]
    flag = False
    for i in range(0, N):
        if  0 == K:
            break
        if  base != S[i] and  (not  flag):
            flag=True
            S[i]=base
        elif  S[i] != base and  flag:
            S[i]=base
        elif  S[i] == base and  flag:
            flag=False
            K -= 1
        else:
            pass
    
    ans=0
    for i in range(0, N-1):
        ans+=S[i+1] == S[i]
    
    print(ans)
  
def __starting_point():
    main()

__starting_point()
