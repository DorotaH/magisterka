def best_choice(n, m):
    if m == 1:
        return 2
    elif m == n:
        return n - 1
    else:
        return (m + n) // 2


# Read input
n, m = map(int, input().split())

# Output the result
print(best_choice(n, m))
