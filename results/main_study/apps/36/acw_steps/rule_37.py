def f(n):
	left, right = -1, 1 + n
	while right - left > 1:
		mid = (left + right) // 2
		x = 6 * mid * (mid + 1) // 2 + 5 * (mid + 1)
		if x > n:
			right = mid
		else:
			left = mid
	if left >= 0:
		mid = left
		x = 6 * mid * (mid + 1) // 2 + 5 * (mid + 1)
		n -= x
	return (n, 1 + left)

def main():
	n = int(input())
	n, k = f(n)
	x = k
	y = -2 * k
	
	d = [k + 1] * 6
	d[1] -= 1
	dx = [1, -1, -2, -1,  1, 2]
	dy = [2,  2,  0, -2, -2, 0]
	
	for i in range(6):
		x += dx[i] * min(d[i], n)
		y += dy[i] * min(d[i], n)
		n = max(0, n - d[i])
	
	print(x, y)


main()
