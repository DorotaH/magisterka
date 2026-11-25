from collections import Counter

N, M = map(int, input().split())
food_counts = Counter()

for _ in range(N):
    K, foods = int(input().split()[0]), list(map(int, input().split()))
    food_counts &= Counter(foods)

print(len(food_counts))
