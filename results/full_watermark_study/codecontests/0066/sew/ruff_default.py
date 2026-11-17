t = int(input())
for _ in range(1, t + 1):
    a, b = map(int, input().split())
    n = 1 + a // 2
    print(b // n)
