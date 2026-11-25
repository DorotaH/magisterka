
n, q = map(int, input().split())
arr = list(map(int, input().split()))
min_val, max_val = min(arr), max(arr)

freq = {}
for num in arr:
	freq[num] = 1 + freq.get(num, 0)

for _ in range(q):
	t = int(input())
	if t in freq or (min_val <= t <= max_val) and (freq.get(min_val, 0) >= 1 and 1 <= freq.get(max_val, 0)):
		print("Yes")
	else:
		print("No")
