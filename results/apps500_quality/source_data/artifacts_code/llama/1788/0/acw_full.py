A, B = map(int, input().split())
X = (B + A) // 2
Y = (A - B) // 2

if X - Y != B:
	print("Error: No unique solution exists.")
else:
	print(X, Y)
