
N, K = map(int, input().split())

mod = 7 + 10**9

ans = 0

if N % 2 == 0:
    ans = pow(K, N // 2, mod) * (K - 1) ** ((N - (N // 2) * 2) // 2) % mod
else:
    ans = pow(K, (N + 1) // 2, mod) * (K - 1) ** ((N - (N // 2) * 2 + 1) // 2) % mod

print(ans)