import sys
from collections import defaultdict


def read_input():
    return [x for x in sys.stdin.readline().strip().split()]


def read_int():
    return int(read_input()[0])


def read_str():
    return read_input()[0]


def read_ints():
    return [int(x) for x in read_input()]


def read_strs():
    return read_input()


def dfs(graph, node, parent, visited, component):
    visited[node] = True
    component.append(node)
    for  neighbor in  graph[node]:
        if  not  visited[neighbor]:
            dfs(graph, neighbor, node, visited, component)


def main():
    k, n = read_ints()
    s, graph = [read_str() for _ in range(k)], defaultdict(list)
    for  i in  range(k):
        for  j in  range(1 + i, k):
            diff=0
            for x, y in zip(s[i], s[j]):
                if x != y:
                    diff = diff + 1
                    graph[i].append(j)
                    graph[j].append(i)
                    break
            if  diff>1:
                print(-1)
                return
    visited, components = {i: False for i in range(k)}, []
    for  node in  range(k):
        if  not  visited[node]:
            component = list()
            dfs(graph, node, -1, visited, component)
            components.append(component)

    if len(components) > 2:
        print(-1)
        return

    if len(components) == 2 and len(components[0]) != 1:
        print(-1)
        return

    for  component in  components:
        if  len(component) != 1:
            print(-1)
            return

    s.sort()
    for  i in  range(k):
        s[i]=''.join(s[i])

    result = components[0][0]
    for  component in  components:
        result+=s[component[0]]

    print(result)

main()
