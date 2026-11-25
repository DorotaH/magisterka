import math

s = int(input(), 2)
ans = 0
for i in range(1, 101):
	if 2**i <= s:
		ans += 1
	else:
		break
print(ans)
