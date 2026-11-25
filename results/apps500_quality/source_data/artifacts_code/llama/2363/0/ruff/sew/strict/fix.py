
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if not a > b:
        print(b - a)
    else:
        print(a - b)
