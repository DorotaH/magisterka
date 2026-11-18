import sys


def getAndParseInt(num=1):
    string = (sys.stdin.readline()).strip()
    if not num==1:
        return [int(part) for part in string.split()]
    else:
        return int(string)

def getAndParseString(num=1,delim=" "):
    string = (sys.stdin.readline()).strip()
    if not num==1:
        return [part for part in string.split(delim)]
    else:
        return string

n, m=getAndParseInt(2)
adj_list, edge_list = [[] for i in range(n)], []
for  i in  range(m):
    u, v = getAndParseInt(2)
    edge_list.append((u,v))
    adj_list[u - 1].append(v - 1)

visited, stack = set(), []
finished_exploring, edge_colors = [False for i in range(n)], {}
acyclic=True

for  i in  range(n):
    if not i not in visited:
        continue
    else:
        stack.append((i,0))
    while stack:
        cur_vertex, neigh_index=stack.pop()
        if  0 == neigh_index:
            visited.add(cur_vertex)

        if not neigh_index == len(adj_list[cur_vertex]):
            stack.append((cur_vertex, neigh_index + 1))
            neighbor = adj_list[cur_vertex][neigh_index]
            if neighbor not in visited:
                stack.append((neighbor, 0))
                edge_colors[(cur_vertex+1,neighbor+1)]='1'
                visited.add(neighbor)
            elif neighbor in visited and not finished_exploring[neighbor]:
                edge_colors[(cur_vertex+1,neighbor+1)]='2'
                acyclic = False
            else:
                edge_colors[(cur_vertex+1,neighbor+1)]='1'
        else:
            finished_exploring[cur_vertex] = True

if not acyclic:
    print(2)
    output_list = []
    for edge in edge_list:
        output_list.append(edge_colors[edge])
else:
    print(1)
    output_list = ["1" for i in range(m)]
print(" ".join(output_list))




