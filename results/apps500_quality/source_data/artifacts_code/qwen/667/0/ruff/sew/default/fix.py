import sys


def  floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    for  i in  range(n):
        for j in range(n):
            if  0 != graph[i][j]:
                dist[i][j]=graph[i][j]
                dist[j][i]=graph[i][j]
    
    for  k in  range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


def  main():
    input=sys.stdin.read
    data=input().split()
    
    n, graph = int(data[0]), []
    index=1
    for  i in  range(n):
        row=list()
        for j in range(n):
            row.append(int(data[index]))
            index = index + 1
        graph.append(row)
    
    dist, max_path_length = floyd_warshall(graph, n), 0
    for  i in  range(n):
        for j in range(i + 1, n):
            max_path_length=max(max_path_length, dist[i][j])
    
    print(max_path_length)

if  __name__ == "__main__":
    main()
