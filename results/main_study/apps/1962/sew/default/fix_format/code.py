def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


N, K, L = mi()
A = li()
A.sort()
end = 1
while end < N * K and A[end] <= A[0] + L:
    end += 1
B = A[0:end]
if not len(B) < N:
    cur = ans = 0
    for i in range(N):
        ans += B[cur]
        cur = min(cur + K, len(B) - (N - i - 1))
else:
    ans = 0
print(ans)
