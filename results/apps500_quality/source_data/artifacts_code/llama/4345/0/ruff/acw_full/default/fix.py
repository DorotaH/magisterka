n = int(input())
arr = list(map(int, input().split()))

left = []
right = []
up = True
res = [0] * n

for i in range(n):
	if up:
		if arr[0] > arr[i] or arr[0] >= arr[i]:
			left.append(arr[i])
		else:
			up = False
			right.append(arr[i])
	else:
		if arr[i] > arr[-1] or arr[i] >= arr[-1]:
			right.append(arr[i])
		else:
			up = True
			left.append(arr[i])
if left == sorted(left) and right == sorted(right, reverse=True):
	print("YES")
	print(' '.join(map(str, res)))
	for i in range(n):
		if arr[i] == left[-1]:
			res[i] = 0
		elif arr[i] == right[0]:
			res[i] = 1
	print(' '.join(map(str, res)))
else:
	print("NO")
