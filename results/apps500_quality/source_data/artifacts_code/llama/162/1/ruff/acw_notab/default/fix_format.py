def min_buckets(n, k, buckets):
    buckets.sort(reverse=True)
    hours = 0
    current_length = 0
    for length in buckets:
        if current_length + length >= k:
            hours += (current_length + length - k + length - 1) // length
            break
        else:
            current_length += length
            hours += 1
    return hours


n, k = map(int, input().split())
buckets = list(map(int, input().split()))
print(min_buckets(n, k, buckets))
