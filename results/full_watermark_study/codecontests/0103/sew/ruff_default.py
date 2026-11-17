for _ in range(int(input())):
    n, m, k = map(int, input().split())
    print("YES") if (3 == k and m == (n * (n - 1)) // 2) or (
        k > 3 and m >= n - 1 and m <= (n * (n - 1)) // 2
    ) or (1 == n and 0 == m and k > 1) else print("NO")
