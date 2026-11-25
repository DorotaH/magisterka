n, k = map(int, input().split())
a = list(map(int, input().split()))

# Find the minimum number of hours required to water the garden
hours = float("inf")
for bucket in a:
	if k % bucket == 0:
		hours = min(hours, k // bucket)

print(hours)
