import heapq as hq
def heap_queue_smallest(nums,n):
  return hq.nsmallest(n, nums)