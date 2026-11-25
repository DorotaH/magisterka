import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

likes = [set() for _ in range(N)]

index = 2
for i in range(N):
	K = int(data[index])
	for j in range(1 + index, K + index + 1):
		likes[i].add(int(data[j]) - 1)
	index += K + 1

common_likes = set.intersection(*likes)
print(len(common_likes))
