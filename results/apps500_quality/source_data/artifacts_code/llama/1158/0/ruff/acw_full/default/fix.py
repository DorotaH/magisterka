from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = Counter(a)
max_count = max(c.values())

total_dishes = (max_count + k - 1) // k

print(sum(c.values()) - 3 * total_dishes)
