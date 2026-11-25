import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))


def count_tracks(start):
	max_coolness = a[start]
	count = 1
	for i in range(1, n):
		track = (i + start) % n
		if max_coolness // 2 > a[track]:
			return count
		max_coolness = max(max_coolness, a[track])
		count += 1
	return -1


results = [count_tracks(i) for i in range(n)]
print(" ".join(map(str, results)))
