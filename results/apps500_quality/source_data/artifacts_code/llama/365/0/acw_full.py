n, x = map(int, input().split())
a = list(map(int, input().split()))

if len(a) != n:
	print('NO')
	exit()

cur = 0
count = 0
for i in a:
	if i + cur > x:
		print('NO')
		exit()
	cur += i
	count += 1
	if cur == x:
		count -= 1
		break

if count > 1:
	print('NO')
else:
	print('YES')
