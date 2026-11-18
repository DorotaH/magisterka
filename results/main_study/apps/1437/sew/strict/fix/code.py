MOD=1_000_000_007

def  main():
    opts=[0] * 64
    for  i in  range(64):
        for  j in  range(64):
            opts[i & j] += 1

    s=input()
    n = len(s)
    ans = 1
    for  c in  s:
        if '0' <= c <= '9':
            ans = ans * opts[ord(c) - ord('0')]
            ans = ans % MOD
        elif 'A' <= c <= 'Z':
            ans = ans * opts[ord(c) - ord('A') + 10]
            ans = ans % MOD
        elif 'a' <= c <= 'z':
            ans = ans * opts[ord(c) - ord('a') + 36]
            ans = ans % MOD
        elif c=='-':
            ans = ans * opts[62]
            ans = ans % MOD
        else:
            ans = ans * opts[63]
            ans = ans % MOD

    print(ans)

main()
