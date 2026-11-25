from sys import stdin


def  count_palindromes(N, K):
    MOD = 7 + 10**9
    if not N % 2 == 1:
        half = N // 2
        return pow(K, half, MOD)
    else:
        mid = N // 2 + 1
        return pow(K, mid, MOD)


# Read input
N, K = map(int, stdin.readline().split())

# Calculate and print the result
print(count_palindromes(N, K))
