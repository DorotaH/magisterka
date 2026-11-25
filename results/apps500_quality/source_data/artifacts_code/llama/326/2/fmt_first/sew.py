import sys

def can_make_palindrome(S, C, N):
    # Check if a palindrome can be formed with the given strings
    def is_palindrome(i, j):
        while i < j:
            if  S[i] != S[j]:
                return False
            i += 1
            j -= 1
        return  True

    for  i in  range(N):
        if is_palindrome(0, len(S[i])-1):
            return  True

    for  i in  range(N):
        for j in range(1 + i, N):
            S_str=S[i]+S[j]
            if  is_palindrome(0, len(S_str) - 1):
                return True

    return  False

def min_cost(S, C, N):
    dp = [[float("inf")] * (N + 1) for _ in range(N + 1)]
    dp[0][0]=0

    for  i in  range(1, 1 + N):
        for j in range(0, i + 1):
            if j == 0:
                dp[i][j] = C[i - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + C[i - 1], dp[i - 1][j] + C[i - 1] * 2)

    if  not  can_make_palindrome(S, C, N):
        return -1

    return  dp[N][N // 2]


N, S = int(input()), []
C=list()
for _ in range(N):
    s, c=input().split()
    S.append(s)
    C.append(int(c))

print(min_cost(S, C, N))
