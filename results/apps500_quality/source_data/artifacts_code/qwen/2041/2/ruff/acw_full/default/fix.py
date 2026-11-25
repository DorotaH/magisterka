

def optimal_subsequence(a: list[int], k: int, pos: int) -> int:
	from heapq import nlargest

	from sortedcontainers import SortedList
	
	# Get the k largest elements
	largest_k = nlargest(k, a)
	
	# Sort these elements
	largest_k.sort()
	
	# Create a sorted list of the remaining elements
	remaining = SortedList(a)
	for num in largest_k:
		remaining.remove(num)
	
	# Get the pos-1 smallest elements from the remaining elements
	smallest_k_minus_1 = remaining[:pos - 1]
	
	# Create a list to store the optimal subsequence
	optimal = []
	for num in largest_k:
		if smallest_k_minus_1 and smallest_k_minus_1[-1] < num:
			optimal.append(smallest_k_minus_1.pop())
		else:
			optimal.append(num)
	
	# The pos-th element in the optimal subsequence
	return optimal[pos - 1]


def main():
	import sys
	input = sys.stdin.read
	data = input().split()
	
	n = int(data[0])
	a = list(map(int, data[1:1 + n]))
	m = int(data[1 + n])
	queries = []
	for i in range(2 + n, len(data), 2):
		k = int(data[i])
		pos = int(data[i + 1])
		queries.append((k, pos))
	
	results = []
	for k, pos in queries:
		result = optimal_subsequence(a, k, pos)
		results.append(result)
	
	for result in results:
		print(result)


if __name__ == "__main__":
	main()
