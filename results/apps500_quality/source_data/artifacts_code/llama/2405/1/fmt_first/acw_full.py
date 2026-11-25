import sys

input = sys.stdin.readline


def update(l, r, val, x, v):
	if l == r:
		tree[x] = min(tree[x], val)
		return
	mid = (l + r) // 2
	if d[2 * x + 1] <= d[x] <= mid:
		update(l, mid, tree[2 * x + 1], 2 * x + 1, v)
	else:
		update(mid + 1, r, tree[2 * x + 2], 2 * x + 2, v)
	tree[x] = min(tree[2 * x + 1], tree[2 * x + 2])


def query(l, r, x, d):
	if l > d or r < d:
		return 0
	if l == r:
		return tree[x]
	mid = (l + r) // 2
	if mid >= d:
		return query(l, mid, 2 * x + 1, d)
	else:
		return query(mid + 1, r, 2 * x + 2, d)


n, k, a, b, q = map(int, input().split())
tree = [10**18] * (4 * n)
d = [0] * (4 * n)
for i in range(n):
	d[i * 2 + 1] = i + 1
	d[i * 2 + 2] = i + 2

for _ in range(q):
	t, *args = map(int, input().split())
	if t == 1:
		d, a = args
		update(0, n - 1, a, 0, d - 1)
	else:
		p = args[0]
		ans = 0
		if p - 1 >= k:
			ans += query(0, n - 1, 0, p - k - 1)
			ans += (p - k - 1 - query(0, n - 1, 0, p - k - 1)) * b
		else:
			ans += query(0, n - 1, 0, p - 1)
		print(ans)
