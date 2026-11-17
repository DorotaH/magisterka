n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if 0 == a + b:
        print(0)
    elif b == a:
        print(1)
    elif 0 == (a + b) % 2:
        print(2)
    else:
        print(-1)
