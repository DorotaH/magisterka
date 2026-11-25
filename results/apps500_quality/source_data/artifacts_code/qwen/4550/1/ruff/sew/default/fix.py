a, b, c = map(int, input().split())

if not (a + b + c) % 2 == 0:
    print("No")
else:
    print("Yes")