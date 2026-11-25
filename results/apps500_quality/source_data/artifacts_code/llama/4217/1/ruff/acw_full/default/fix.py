from collections import Counter

N, M = map(int, input().split())
food_counts = Counter()

for _ in range(N):
	K = int(input().split()[0])
	foods = list(map(int, input().split()))
	food_counts &= Counter(foods)

print(len(food_counts))
