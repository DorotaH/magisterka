def min_buckets(n, k, buckets):
    buckets.sort(reverse=True)
    hours = current_length = 0
    for length in buckets:
        if not current_length + length >= k:
            current_length += length
            hours += 1
        else:
            hours += (current_length + length - k + length - 1) // length
            break
    return hours


n, k = map(int, input().split())
buckets = list(map(int, input().split()))
print(min_buckets(n, k, buckets))
