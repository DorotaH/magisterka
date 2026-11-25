
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 0
left = -10**18
for right in arr:
	while left < right:
		left += 1
		if abs(left - right) in arr and abs(left + right) in arr:
			ans += 1
	if abs(left - right) in arr and abs(left + right) in arr:
		ans += 1
	left += 1

print(ans)
