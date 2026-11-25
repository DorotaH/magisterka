from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

utensils_counts = Counter(a)

max_per_person = max(utensils_counts.values())
min_stolen = sum(utensils_counts.values()) - (max_per_person * k)

min_stolen = max(min_stolen, 0)

print(min_stolen)
