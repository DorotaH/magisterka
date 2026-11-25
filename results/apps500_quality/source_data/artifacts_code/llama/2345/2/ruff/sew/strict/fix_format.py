for _ in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    subset = [i + 1 for i in range(n) if a[i] == n - 1 - i]
    print(len(subset))
    print(*subset)
