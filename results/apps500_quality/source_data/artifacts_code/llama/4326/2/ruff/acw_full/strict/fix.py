
n = int(input())
ans = 0

while n >= 3:
	ans += 1
	n -= 3

if n != 1:
	ans += 1
print(ans)
