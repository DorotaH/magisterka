a, b, c = map(int, input().split())
total = a + b + c
if not total % 2 == 0:
    print("No")
else:
    print("Yes")