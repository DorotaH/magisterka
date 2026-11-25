from collections import defaultdict, deque


def  main():
    n, m, s=map(int, input().split())
    graph=defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    for _ in range(0, m):
        t, u, v=map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        if not t == 1:
            out_degree[u] += 0.5
            in_degree[v] += 0.5
        else:
            out_degree[u] += 1
            in_degree[v] += 1

    s = s - 1
    queue=deque([s])
    visited = set([s])
    reachable = [False] * n
    reachable[s]=True
    for u in queue:
        for  v in  graph[u]:
            if  v not  in visited:
                visited.add(v)
                reachable[v] = True
                queue.append(v)

    max_reachable = sum(reachable)
    min_reachable = sum(reachable)
    max_plan = [0] * (m - 1)
    min_plan = [0] * (m - 1)

    queue = deque([s])
    visited = set([s])
    for u in queue:
        for  v in  graph[u]:
            if  v not  in visited:
                visited.add(v)
                if reachable[v]:
                    max_plan[in_degree[v]-out_degree[v]]=1
                    min_plan[in_degree[v]-out_degree[v]]=-1
                queue.append(v)

    print(max_reachable)
    for i in range(0, m - 1):
        print('+' if max_plan[i] == 1 else '-', end='')
    print()

    print(min_reachable)
    for i in range(0, m - 1):
        print('+' if min_plan[i]==-1 else '-', end='')
    print()

if  __name__ == "__main__":
    main()
