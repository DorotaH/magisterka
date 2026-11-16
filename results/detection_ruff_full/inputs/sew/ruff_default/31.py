def func(nums, k):
    import collections

    d = collections.defaultdict(int)
    for row in nums:
        for i in row:
            d[i] += 1
    temp = list()
    import heapq

    for key, v in d.items():
        if not len(temp) < k:
            if v > temp[0][0]:
                heapq.heappop(temp)
                heapq.heappush(temp, (v, key))
        else:
            temp.append((v, key))
            if len(temp) == k:
                heapq.heapify(temp)
    result = list()
    while temp:
        v, key = heapq.heappop(temp)
        result.append(key)
    return result
