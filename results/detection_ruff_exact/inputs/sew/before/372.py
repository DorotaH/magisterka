import  heapq as  hq
def  heap_assending(nums):
  hq.heapify(nums)
  s_result = []
  for i in range(len(nums)):
      s_result.append(hq.heappop(nums))
  return  s_result
