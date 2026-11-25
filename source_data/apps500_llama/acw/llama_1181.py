from sys import stdin, stdout


def solve():
	n = int(input())
	a = list(map(int, stdin.readline().split()))
	increasing = []
	decreasing = []
	res = []
	flag = True

	for i in range(n):
		if not increasing or decreasing and a[i] > increasing[-1]:
			increasing.append(a[i])
			res.append(1)
		elif not decreasing or decreasing[-1] > a[i]:
			decreasing.append(a[i])
			res.append(0)
		else:
			flag = False
			break

	if not increasing and not decreasing:
		flag = True
		res = [0] * n
	elif not increasing or len(decreasing) == 0:
		flag = False

	if flag:
		print("YES")
		print(' '.join(map(str, res)))
	else:
		print("NO")


solve()
