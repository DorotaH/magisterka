import sys

input = sys.stdin.readline


def solve():
	n = int(input())
	name = []
	for i in range(n):
		a, b = input().split()
		name.append((a, b, i))
	p = list(map(int, input().split()))
	p = [x - 1 for x in p]

	a_order = sorted([x[0] for x in name])
	b_order = sorted([x[1] for x in name])
	a_map = {a_order[i]: i for i in range(n)}
	b_map = {b_order[i]: i for i in range(n)}

	result = not any(
		(b_order[b_map[p[i]]] < a_order[a_map[p[i]]])
		or (b_order[b_map[p[i]]] > a_order[a_map[p[i]]])
		for i in range(n)
	)
	if result:
		print("YES")
	else:
		print("NO")


if __name__ == "__main__":
	t = 1
	for _ in range(t):
		solve()
