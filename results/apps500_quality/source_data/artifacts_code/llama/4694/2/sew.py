n = int(input())
a = list(map(int, input().split()))

total_distance = sum(a)

min_distance = float('inf')
for i in range(len(a)):
    distance = abs(a[i] - a[0]) + (sum(a[:i]) + sum(a[i+1:]))
    min_distance = min(min_distance, distance)

print(min_distance)