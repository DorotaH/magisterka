n, x = map(int, input().split())
arr = list(map(int, input().split()))
mex = 0
current = 0
operations = 0

while mex < x:
	if current < x and current not in arr:
		mex += 1
	elif current not in arr:
		operations += 1
		arr.remove(current)
		mex += 1
	current += 1

print(operations)
