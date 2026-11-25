S = input()
n = len(S)

if not n == 1:
    painted = 0
    for i in range(1, n):
        if S[i] == S[i - 1]:
            painted += 1
    print(painted)
else:
    print(0)