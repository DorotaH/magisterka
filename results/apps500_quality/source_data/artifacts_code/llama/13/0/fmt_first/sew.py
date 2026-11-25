from collections import deque, defaultdict

def find_order(n, main_courses):
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        dependencies=list(map(int, input().split()))[1:]
        for dependency in dependencies:
            graph[dependency].append(i)
            indegree[i] += 1

    queue = deque([course for course in main_courses if indegree[course] == 0])
    visited = set()
    order=list()

    for course in queue:
        order.append(course)
        visited.add(course)

        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if  0 == indegree[neighbor]:
                queue.append(neighbor)
                visited.add(neighbor)

    if len(order) != len(main_courses):
        print(-1)
    else:
        print(len(order))
        print(" ".join(map(str, order)))


n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
find_order(n, main_courses)
