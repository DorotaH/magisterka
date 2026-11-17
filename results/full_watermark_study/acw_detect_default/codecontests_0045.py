t = int(input())
while t:
	n = int(input())
	arr = [int(i) for i in input().split()]
	x = -1
	# k=-2
	if arr[n - 1] == 0:
		for i in range(1, 1 + n):
			print(i, end=" ")
		print(1 + n)
	else:
		for k in range(n - 2, -1, -1):
			if arr[k] == 0:
				x = k
				break
		# print(k)
		# if k==-1:
		# 	print(-1)
		# else:
		for i in range(1, 2 + x):
			print(i, end=" ")
		print(1 + n, end=" ")
		for i in range(2 + x, n):
			print(i, end=" ")
		print(n)
	t -= 1
