from collections import defaultdict, deque


def topological_sort(n, k, main_courses, dependencies):
	in_degree = [0] * (1 + n)
	graph = defaultdict(list)

	for i in range(1, 1 + n):
		for dep in dependencies[i - 1]:
			graph[dep].append(i)
			in_degree[i] += 1

	queue = deque(list(main_courses))
	visited = set(main_courses)
	result = []

	while queue:
		course = queue.popleft()
		result.append(course)

		for neighbor in graph[course]:
			in_degree[neighbor] -= 1
			if in_degree[neighbor] == 0 and neighbor not in visited:
				queue.append(neighbor)
				visited.add(neighbor)

	return (len(result), result) if len(result) == n else -1


# Read input
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split())) for _ in range(n)]

# Output result
result = topological_sort(n, k, main_courses, dependencies)
if result == -1:
	print(result)
else:
	print(result[0])
	print(*result[1])
