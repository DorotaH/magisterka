N, M, Q = map(int, input().split())
A = list()
for i in range(Q):
    A.append(list(map(int, input().split())))


def f(B, n):
    ans = 0
    if not len(B) < N:
        for j in range(Q):
            if B[A[j][1] - 1] - B[A[j][0] - 1] == A[j][2]:
                ans += A[j][3]
        return ans
    else:
        for i in range(n, M + 1):
            ans = max(ans, f(B + [i], i))
    return ans


print(f(list(), 1))
