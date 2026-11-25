from collections import defaultdict, deque


def topological_sort(n, k, main_courses, dependencies):
    in_degree = [0] * (1 + n)
    graph = defaultdict(list)

    for i in range(1, 1 + n):
        for j in dependencies[i - 1]:
            graph[j].append(i)
            in_degree[i] += 1

    queue = deque([i for i in range(1, 1 + n) if in_degree[i] == 0])
    result = []
    count = 0

    while queue:
        course = queue.popleft()
        result.append(course)
        count += 1

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if count < k + len(main_courses):
        return -1

    main_course_order = [course for course in main_courses if course in result]
    return len(result), result, main_course_order


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    k = int(data[1])
    main_courses = list(map(int, data[2:2 + k]))
    dependencies = [list(map(int, data[2 + k + i * 2:2 + k + (i * 2 + 1)])) for i in range(n)]

    result_count, result_order, main_course_order = topological_sort(n, k, main_courses, dependencies)

    if result_count == -1:
        print(-1)
    else:
        print(result_count)
        print(" ".join(map(str, result_order)))


if __name__ == "__main__":
    main()
