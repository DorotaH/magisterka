t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if not (n < k or (n - k) % 2 != 0):
        print("YES")
    else:
        print("NO")
