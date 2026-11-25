S = input()
n = len(S)

if n == 1:
    print(0)
else:
    painted = 0
    for i in range(1, n):
        if S[i] == S[i - 1]:
            painted += 1
    print(painted)
