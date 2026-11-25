
n, k = map(int, input().split())
buckets = list(map(int, input().split()))

max_bucket = max(buckets)
best_bucket = [0] * (k + 1)
best_bucket[0] = 1
for i in range(1, k + 1):
    best_bucket[i] = 1 + best_bucket[i - 1]
    for j in range(n):
        if buckets[j] <= i:
            best_bucket[i] = max(best_bucket[i], 1 + best_bucket[i - buckets[j]])

print(best_bucket[k])
