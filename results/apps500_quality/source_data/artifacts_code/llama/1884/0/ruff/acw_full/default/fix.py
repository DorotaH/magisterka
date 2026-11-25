

def can_deploy_service(c, x, k):
	n = len(c)
	c.sort()
	c.reverse()
	target = x / k
	for i in range(n):
		if c[i] < target:
			return False
		k = (c[i] // target) + (c[i] % target > 0)
	return True


def main():
	n, x1, x2 = map(int, input().split())
	c = list(map(int, input().split()))

	for i in range(1, 1 + n):
		if can_deploy_service(c, x1, i) and can_deploy_service(c, x2, n - i):
			k1, k2 = i, n - i
			used = [0] * (1 + n)
			for j in range(n):
				if x1 / i <= c[j]:
					used[1 + j] = 1
			for j in range(n):
				if x2 / (n - i) <= c[j]:
					used[1 + j] = 2
			print('Yes')
			print(k1, k2)
			for i in range(1, 1 + n):
				if used[i] == 1:
					print(i, end=' ')
			print()
			for i in range(1, 1 + n):
				if used[i] == 2:
					print(i, end=' ')
			return
	print('No')


if __name__ == "__main__":
	main()
