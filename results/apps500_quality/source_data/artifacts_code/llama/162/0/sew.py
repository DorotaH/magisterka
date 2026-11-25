import  math

n, k = map(int, input().split())
buckets = list(map(int, input().split()))

max_bucket = max(buckets)
best_bucket = [0] * (k + 1)
best_bucket[0] = 1
for i in range(1, 1 + k):
    best_bucket[i]=1 + best_bucket[i - 1]
    for  j in  range(0, n):
        if  i >= buckets[j]:
            best_bucket[i]=max(best_bucket[i], 1 + best_bucket[i - buckets[j]])

print(best_bucket[k])