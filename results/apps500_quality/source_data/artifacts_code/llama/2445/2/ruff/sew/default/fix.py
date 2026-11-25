def min_turns(n):
    return (n + 1) // 2 + (n - 1) // 2

t = int(input())
for _ in range(t):
    n = int(input())
    print(min_turns(n))