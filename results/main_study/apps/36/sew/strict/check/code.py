def f(n):
	left = -1
	right = n + 1
	while  right - left > 1:
		mid=(left + right)//2
		x=6 * mid * (mid + 1) // 2+5 * (mid + 1)
		if not x > n:
			left = mid
		else:
			right = mid
	if left >= 0:
		mid = left
		x = 6 * mid * (mid + 1) // 2 + 5 * (mid + 1)
		n -= x
	return (n, left + 1)


def main():
	n = int(input())
	n, k = f(n)
	x = k
	y = -2 * k
	
	d = 6 * [k + 1]
	d[1] -= 1
	dx = [1, -1, -2, -1,  1, 2]
	dy = [2,  2,  0, -2, -2, 0]
	
	for i in range(6):
		x+=min(d[i], n)*dx[i]
		y+=min(d[i], n)*dy[i]
		n=max(0, n-d[i])
	
	print(x, y)


main()
