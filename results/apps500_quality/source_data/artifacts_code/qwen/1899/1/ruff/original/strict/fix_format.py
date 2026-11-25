from collections import defaultdict
from heapq import heappop, heappush


def kth_order_statistic(n, s, m, k, a, segments):
    # Create a list to store the frequency of each element in the segments
    freq = [0] * (n + 1)

    # Create a dictionary to store the elements in each segment
    segment_elements = defaultdict(list)

    # Fill the frequency list and segment_elements dictionary
    for l, r in segments:
        for i in range(l - 1, r):
            freq[i] += 1
            heappush(segment_elements[i], a[i])

    # Create a list to store the elements that appear at least k times
    k_elements = []

    # Iterate over the frequency list
    for i in range(n):
        # If the frequency of the current element is at least k, add it to the k_elements list
        if freq[i] >= k:
            k_elements.append(heappop(segment_elements[i]))

    # If there are fewer than k elements in the k_elements list, return -1
    if len(k_elements) < k:
        return -1

    # Return the k-th element in the sorted k_elements list
    return k_elements[k - 1]


# Read input
n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(s)]

# Print the result
print(kth_order_statistic(n, s, m, k, a, segments))
