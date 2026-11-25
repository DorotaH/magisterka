import sys
from collections import defaultdict, deque


def  topological_sort(n, k, main_courses, dependencies):
    in_degree, adj_list = [0] * (n + 1), defaultdict(list)

    for course in range(1, n + 1):
        for dep in dependencies[course-1]:
            adj_list[dep].append(course)
            in_degree[course] += 1

    queue, result = deque([course for course in range(1, n + 1) if course not in adj_list]), []
    visited=set()

    while  queue:
        current = queue.popleft()
        result.append(current)
        visited.add(current)

        for  neighbor in  adj_list[current]:
            in_degree[neighbor] -= 1
            if  in_degree[neighbor] == 0:
                queue.append(neighbor)

    if  len(result) != n:
        return  -1

    main_passed=0
    for course in result:
        if  course in  main_courses:
            main_passed += 1
        if  k == main_passed:
            return (len(result), result)

    return -1


def  main():
    input=sys.stdin.read
    data=input().split()

    n, k = int(data[0]), int(data[1])
    main_courses=list(map(int, data[2:k+2]))

    dependencies, index = [], 2 + k
    for i in range(n):
        t=int(data[index])
        dependencies.append(list(map(int, data[1+index:1+index+t])))
        index+=1 + t

    result=topological_sort(n, k, main_courses, dependencies)

    if not result == -1:
        print(result[0])
        print(' '.join(map(str, result[1])))
    else:
        print(-1)

if __name__ == "__main__":
    main()
