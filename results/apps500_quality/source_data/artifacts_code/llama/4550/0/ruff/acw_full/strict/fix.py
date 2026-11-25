a, b, c = map(int, input().split())
total = a + b + c

if total % 2 == 0 and (a % 2 == 0 or b % 2 == 0 or c % 2 == 0):
	print("Yes")
else:
	print("No")
