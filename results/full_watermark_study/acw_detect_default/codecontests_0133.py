a = [0]
s = "M"
n = int(input())
a.extend(list(map(int, input().split())))
s = input() + s
a_part_sorted = sorted(a[1:])
a[1:] = a_part_sorted
r = n
l = 1
ans = [0] * (1 + n)
for i in range(n, 0, -1):
	if s[i] == s[i - 1]:
		ans[i] = l
		l = l + 1
	else:
		ans[i] = r
		r = r - 1
for i in range(1, 1 + n):
	print(a[ans[i]], "R" + " " if (ans[i] & 1) ^ (n & 1) ^ (s[n] == "R") else "L")
