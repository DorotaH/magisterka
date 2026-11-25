import sys


def solve():
	n = int(input())
	a = [int(x) for x in input().split()]

	ans = [-1] * n
	for i in range(n):
		left, right = i, i
		while 0 < left and a[left - 1] >= a[i]:
			left -= 1
		while 1 + right < n and a[1 + right] >= a[i]:
			right += 1
		k = right - left + 1
		j = (i + n - 1) % n
		if 2 * a[j] < a[i]:
			ans[i] = k
		else:
			m = 0
			while (m + j) % n != i:
				m += 1
				if 2 * a[(m + j - 1) % n] < a[i]:
					ans[i] = k + m
					break
				if 2 * a[(m + j) % n] < a[i]:
					ans[i] = k + m + 1
					break
				m += 1
				if 2 * a[(m + j) % n] < a[i]:
					ans[i] = k + m
					break
			if ans[i] == -1:
				ans[i] = -1 if k == n else k

	print(' '.join(map(str, ans)))


if __name__ == "__main__":
	solve()
