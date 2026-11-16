import heapq
from collections import Counter
def  rearange_string(S):
    ctr = Counter(S)
    heap = []
    for key, value in ctr.items():
        heap.append((-value, key))
    heapq.heapify(heap)
    if  2 * (-heap[0][0])>1 + len(S): 
        return  ""
    ans = []
    while  len(heap) >= 2:
        nct1, char1=heapq.heappop(heap)
        nct2, char2=heapq.heappop(heap)
        ans.extend([char1, char2])
        if  nct1 + 1: heapq.heappush(heap, (1 + nct1, char1))
        if  nct2 + 1: heapq.heappush(heap, (1 + nct2, char2))
    return  "".join(ans) + (heap[0][1] if  heap else "")