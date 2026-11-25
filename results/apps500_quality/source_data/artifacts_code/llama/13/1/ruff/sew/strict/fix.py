from collections import deque


def main():
    n, k=map(int, input().split())
    main_courses = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree=[0]*(n + 1)
    for i in range(1, 1 + n):
        dependencies = list(map(int, input().split()))
        if dependencies[0] == 0:
            graph[0].append(i)
        for  j in  range(1, dependencies[0] + 1):
            graph[dependencies[j]].append(i)
            indegree[i] += 1

    queue=deque()
    for course in main_courses:
        queue.append(course)
        indegree[course] = -1

    result = []
    count = 0
    while  queue:
        course=queue.popleft()
        result.append(course)
        count = count + 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if  indegree[neighbor] == 0:
                queue.append(neighbor)

    if not count < k:
        print(count)
        print(*result)
    else:
        print(-1)

main()
