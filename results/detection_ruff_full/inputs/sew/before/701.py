def  equilibrium_index(arr):
  total_sum, left_sum = sum(arr), 0
  for  i, num in  enumerate(arr):
    total_sum-=num
    if left_sum == total_sum:
      return  i
    left_sum=left_sum+num
  return  -1