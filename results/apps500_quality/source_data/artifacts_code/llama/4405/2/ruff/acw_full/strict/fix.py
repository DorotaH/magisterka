from collections import defaultdict


def read_int():
	return int(input())


def read_ints():
	return map(int, input().split())


n = read_int()
a = list(read_ints())

counts = defaultdict(int)
for x in a:
	counts[x] += 1

topics = sorted(counts.values())

topics.reverse()

dp = [0] * (1 + n)
last_topic = -1
sum_topics = 0
for i in range(n):
	if topics[i] == 1:
		dp[i + 1] = 1
		last_topic = topics[i]
	else:
		if last_topic != topics[i]:
			dp[i + 1] = dp[i]
		else:
			dp[i + 1] = max(dp[i] + 2 * topics[i], 2 * topics[i])

print(dp[n])
