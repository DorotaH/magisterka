A1, A2, A3 = map(int, input().split())
if not A1 + A2 + A3 >= 22:
    print("win")
else:
    print("bust")