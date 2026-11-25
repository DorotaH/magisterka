D, T, S = map(int, input().split())
time_required = D / S
if T >= time_required:
	print("Yes")
else:
	print("No")
