from sys import stdin


def count_palindromes(N, K):
    MOD = 7 + 10**9
    if N % 2 == 1:
        mid = 1 + N // 2
        return pow(K, mid, MOD)
    else:
        half = N // 2
        return pow(K, half, MOD)


# Read input
N, K = map(int, stdin.readline().split())

# Calculate and print the result
print(count_palindromes(N, K))
