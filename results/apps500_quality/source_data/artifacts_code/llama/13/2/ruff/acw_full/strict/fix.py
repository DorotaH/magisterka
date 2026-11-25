from collections import defaultdict, deque


def topological_sort(graph, main_courses):
	visited = [False] * (1 + n)
	order = []
	queue = deque(list(main_courses))

	while queue:
		course = queue.popleft()
		if not visited[course]:
			visited[course] = True
			order.append(course)
			for neighbor in graph[course]:
				if not visited[neighbor]:
					queue.append(neighbor)

	if k > len(order):
		return -1, []

	for course in order:
		if course not in main_courses:
			order.remove(course)

	return len(order), order


n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(1, 1 + n):
	deps = list(map(int, input().split()))
	if deps[0] > 0:
		graph[i].extend(deps[1:])

ans, order = topological_sort(graph, main_courses)
print(ans)
if ans != -1:
	print(*order)
