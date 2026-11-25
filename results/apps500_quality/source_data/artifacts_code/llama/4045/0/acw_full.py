n = int(input())
s = input()
t = input()

if s != t and (s in t or t in s) or s == t:
	print("NO")
else:
	print("YES")
	a = ['a'] * n
	b = ['b'] * n
	c = ['c'] * n
	res = []
	for _ in range(3):
		res += a
		res += b
		res += c
	print("".join(res))
