n = int(input())
ans = 0

while 3 <= n:
	n -= 3
	ans += 1

if 0 < n:
	ans += n // 2

print(ans)
