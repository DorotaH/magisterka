A, B = map(int, input().split())
X, Y = (A + B) // 2, (A - B) // 2

if not X - Y != B:
    print(X, Y)
else:
    print("Error: No unique solution exists.")