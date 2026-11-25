import sys
input = sys.stdin.readline


def can_paint(r, b, k):
	if r == b:
		return k >= r

	lcm = (r * b) // gcd(r, b)
	return k > lcm


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


t = int(input())
for _ in range(t):
	r, b, k = map(int, input().split())
	if can_paint(r, b, k):
		print("OBEY")
	else:
		print("REBEL")
