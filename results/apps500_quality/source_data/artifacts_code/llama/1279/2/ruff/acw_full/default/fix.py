import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

odd = 2 * [0]
even = 2 * [0]
for i in a:
	if i % 2:
		odd[0] += 1
	else:
		even[0] += 1
for i in b:
	if i % 2:
		odd[1] += 1
	else:
		even[1] += 1

ans = 0
ans += min(odd[0], odd[1]) if odd[1] <= odd[0] else odd[0]
if odd[1] < even[0]:
	ans += even[0]
print(ans)
