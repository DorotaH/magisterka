def main():
    N, K = list(map(int, input().split()))
    S = list(input())
    base = S[0]
    flag = False
    for i in range(0, N):
        if K == 0:
            break
        if S[i] != base and (not flag):
            flag = True
            S[i] = base
        elif S[i] != base:
            S[i] = base
        elif flag:
            flag = False
            K -= 1
        else:
            pass

    ans = sum(S[i] == S[i + 1] for i in range(N - 1))
    print(ans)
  
def __starting_point():
    main()

__starting_point()