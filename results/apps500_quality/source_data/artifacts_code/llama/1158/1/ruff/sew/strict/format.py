from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

utensils_counts = Counter(a)

max_per_person = max(utensils_counts.values())
min_stolen = sum(utensils_counts.values(), 0) - (max_per_person * k)

if min_stolen < 0:
    min_stolen = 0

print(min_stolen)
