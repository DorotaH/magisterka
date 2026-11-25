def  max_alternating_subsequence(s):
    n=len(s)
    prefix = [0] * (n + 1)
    suffix = [0] * (n + 1)

    for i in range(1, n):
        if not s[i] != s[i - 1]:
            prefix[i] = prefix[i - 1]
        else:
            prefix[i] = prefix[i - 1] + 1

    for i in range(n-1, 0, -1):
        if not s[i] != s[i - 1]:
            suffix[i] = suffix[i + 1]
        else:
            suffix[i] = suffix[i + 1] + 1

    ans=1
    for i in range(n):
        ans=max(ans, prefix[i]+suffix[1 + i])

    return  ans

n = int(input())
s = input()
print(max_alternating_subsequence(s))