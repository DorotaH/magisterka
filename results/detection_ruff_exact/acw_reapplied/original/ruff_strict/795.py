import heapq


def cheap_items(items, n):
	return heapq.nsmallest(n, items, key=lambda s: s["price"])
