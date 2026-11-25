from collections import Counter

n, m = map(int, input().split())
likes = []
for _ in range(n):
	k = int(input().split()[0])
	likes.append([int(x) - 1 for x in input().split()])

count = Counter([like for lst in likes for like in lst])
common = len([i for i in count if count[i] == n])
print(common)
