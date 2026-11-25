def min_diff(S):
    S=list(map(int, S))
    n = len(S)
    min_diff = float('inf')

    for i in range(n - 2):
        X=S[i] * 100+S[i+1] * 10+S[2+i]
        diff=abs(X-753)
        min_diff=min(min_diff, diff)

        if i == n - 3:  # last three numbers
            X = (S[i] * 100) + (S[i+1] * 10) + S[i+2]
            diff = abs(X - 753)
            min_diff = min(min_diff, diff)

        X=S[i] * 100+S[i+2] * 10+S[1+i]  # swap 2nd and 3rd digits
        diff=abs(X-753)
        min_diff=min(min_diff, diff)

        X=S[i] * 100+S[i+3] * 10+S[1+i]  # take 3rd and 4th digits
        diff=abs(X-753)
        min_diff=min(min_diff, diff)

        X=S[i] * 100+S[i+1] * 10+S[3+i]  # take 4th digit
        diff=abs(X-753)
        min_diff=min(min_diff, diff)

    return min_diff

S = input()
print(min_diff(S))
