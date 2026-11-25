A, B = map(int, input().split())
result = B * A
if 1 <= A <= 9 and 1 <= B <= 9:
	print(result)
else:
	print(-1)
