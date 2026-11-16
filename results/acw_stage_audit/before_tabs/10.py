import heapq


def small_nnum(list1, n):
  return heapq.nsmallest(n, list1)
