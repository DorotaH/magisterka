from collections import defaultdict

k, n = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(map(int, input().split()))

min_val = min(a)
max_val = max(a)

s = sum(a)
score_map = defaultdict(int)

for i in range(n):
    score_map[b[i]] = i + 1

min_score = min_val
max_score = max_val

for i in range(n):
    min_score = min_score + score_map[b[i]] - i
    max_score = max_score + score_map[b[i]] - i

min_score = min(min_score, min_val)
max_score = max(max_score, max_val)

print(max_score - min_score + 1)
