test = int(input())
for _ in range(test):
    s, n, k = map(int, input().split())
    if k > s:
        print("NO")
    elif s == k:
        print("YES")
    else:
        s -= n
        s -= k * (n // k)
        if s >= 0:
            print("NO")
        else:
            print("YES")
